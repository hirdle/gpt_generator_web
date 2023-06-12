from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Channel, Image
from .forms import ChannelForm, ImageForm




def index(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration.html', {'form': form})




@login_required
def channels_view(request):
    channels = Channel.objects.filter(owner=request.user)
    return render(request, 'channels.html', {"channels": channels})



@login_required
def channel_update(request, id):

    channel = get_object_or_404(Channel, pk=id)
    if channel.owner != request.user:
        raise Http404

    
    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES, instance=channel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return redirect('channel_update', id=id)
        
    else:
        form = ChannelForm(instance=channel)

    return render(request, 'channel_update.html', {'form': form, "channel": channel})




@login_required
def image_delete(request, id):

    image = get_object_or_404(Image, pk=id)
    if image.owner != request.user:
        raise Http404
    
    image.delete()

    return redirect('images_update', id=image.channel.id)
    


@login_required
def images_update(request, id):

    channel = get_object_or_404(Channel, pk=id)
    if channel.owner != request.user:
        raise Http404
    
    images = Image.objects.filter(channel__id=channel.id)

    split_themes = list(filter(None, channel.themes.strip().split("\n")))

    themes = "<br>".join([f'{i+1}. {split_themes[i]}' for i in range(len(split_themes))])

    if len(split_themes) == 0: themes = ''

    
    if request.method == 'POST':
            
        form = ImageForm(request.POST, request.FILES)
        

        if form.is_valid():

            image = form.save(commit=False)


            image.owner = request.user 
            image.channel = channel
            image.theme = split_themes[form.cleaned_data['theme_id']-1]
            image.save()

            
            messages.success(request, 'Данные успешно обновлены!')
            return redirect('images_update', id=id)
         
    else:
        form = ImageForm()


    return render(request, 'image_update.html', 
                  {'form': form, "images": images, 
                   "channel": channel, 
                   "themes": themes, 
                   "max_themes_id": len(split_themes)
                   })

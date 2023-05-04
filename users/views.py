from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Channel
from .forms import ChannelForm

from rest_framework import generics, permissions
from .serializer import ChannelSerializer

from rest_framework.generics import RetrieveAPIView

class ChannelDetailView(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


from rest_framework.generics import RetrieveUpdateAPIView

class ChannelUpdateView(RetrieveUpdateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelListView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    http_method_names = ['get']



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
def index(request):
    channels = Channel.objects.filter(owner=request.user)
    return render(request, 'index.html', {"channels": channels})


@login_required
def channel_update(request, id):

    channel = get_object_or_404(Channel, pk=id)
    if channel.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return redirect('channel_update', id=id)
    else:
        form = ChannelForm(instance=channel)
    return render(request, 'channel_update.html', {'form': form, "channel": channel})



def edit_channel(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ChannelForm(instance=channel)
    
    return render(request, 'edit_channel.html', {'form': form})
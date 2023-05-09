from django.contrib.auth.models import User
from users.models import Channel, Image

from rest_framework import generics, permissions
from .serializer import ChannelSerializer, ImageSerializer

from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveDestroyAPIView


class ChannelDetailView(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelUpdateView(RetrieveUpdateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelListView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    http_method_names = ['get']


class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get']


class ImageDetailView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDeleteView(RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
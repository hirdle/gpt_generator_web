from django.urls import path
from .views import ChannelListView, ChannelDetailView, ChannelUpdateView, ImageListView, ImageDeleteView, ImageDetailView

urlpatterns = [
    path('images/', ImageListView.as_view()),
    path('images/<int:pk>/', ImageDetailView.as_view()),
    path('images/<int:pk>/delete/', ImageDeleteView.as_view()),

    path('channels/', ChannelListView.as_view()),
    path('channels/<int:pk>/', ChannelDetailView.as_view()),
    path('channels/<int:pk>/update/', ChannelUpdateView.as_view()),
]


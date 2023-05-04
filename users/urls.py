from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, index, channel_update, ChannelListView, ChannelDetailView, ChannelUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register_view, name='register'),
    path('', index, name='index'),
    path('<int:id>/', channel_update, name='channel_update'),

    path('api/channels/', ChannelListView.as_view()),
    path('api/channels/<int:pk>/', ChannelDetailView.as_view()),
    path('api/channels/<int:pk>/update/', ChannelUpdateView.as_view()),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, channels_view, channel_update, images_update, image_delete, index

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register_view, name='register'),
    path('channels/', channels_view, name='channels'),

    path('', index, name='index'),

    path('channels/<int:id>/', channel_update, name='channel_update'),
    
    path('images/<int:id>/', images_update, name='images_update'),
    # path('images/<int:id>/multiply/', images_multiply_update, name='images_multiply_update'),
    path('images/<int:id>/delete/', image_delete, name='images_delete'),
]


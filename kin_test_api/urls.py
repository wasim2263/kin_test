from django.urls import path
from .views import UserProfileView, user_profile_update
from rest_framework import routers
from django.conf.urls import url, include



urlpatterns = [
    path(r'profile/', UserProfileView.as_view(), name= 'user_profile_get'),
    path('profile/update/', user_profile_update, name='user_profile_update'),

]
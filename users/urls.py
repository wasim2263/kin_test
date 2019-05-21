from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'users'

urlpatterns = [
    # ex: /
    path('profile/', views.profile, name='profile'),
    # path('unused-languages', views.filterLnaguage, name='unused.languages'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_menu, name='menu'),
    path("gallery/<int:pk>/", gallery_menu, name='gallery-menu'),


]

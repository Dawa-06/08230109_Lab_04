# Import the path function to define URL routes
from django.urls import path

# Import the views file (where the functions for each page are written)
from . import views

# URL patterns for the learning journey application
urlpatterns = [
    # Main learning journey page (homepage)
    path('', views.Index, name='Index'),
    
    # About Me page
    path('about/', views.aboutMe, name='aboutMe'),
]
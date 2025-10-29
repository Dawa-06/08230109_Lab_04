# Import the render function to display HTML templates
from django.shortcuts import render


# Import the models to access data from the database
from .models import AboutMe, LearningJourney

def Index(request):
   
    # Retrieve all learning journey entries from the database
    journeys = LearningJourney.objects.all()
    
    # Render the Index template with the journey data
    return render(request, 'index.html', {'journeys': journeys})


def aboutMe(request):
    
    # Retrieve the first (and typically only) personal information entry
    abouts = AboutMe.objects.all()
    
    # Render the aboutMe template with the personal data
    return render(request, 'aboutme.html', {'abouts': abouts})
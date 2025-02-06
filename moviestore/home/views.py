from django.shortcuts import render
from movies.models import Movie  # Import the Movie model
import random

def index(request):
    template_data = {'title': 'Movies Store'}

    # Fetch all movies and select two random ones
    movies = list(Movie.objects.all())  # Convert QuerySet to list
    random_movies = random.sample(movies, 2) if len(movies) >= 2 else movies  # Pick 2 if possible

    return render(request, "home/index.html", {
        'template_data': template_data,
        'random_movies': random_movies  # Pass movies to the template
    })

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, "home/about.html", {'template_data': template_data})

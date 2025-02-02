from django.shortcuts import render

movies = [
    {'id': 1, 'name': 'Inception', 'price': 12, 'description': 'A mind-bending heist thriller.'},
    {'id': 2, 'name': 'Avatar', 'price': 13,
     'description': 'A journey to a distant world and the battle for resources.'},
    {'id': 3, 'name': 'The Dark Knight', 'price': 14, 'description': 'Gotham’s vigilante faces the Joker.'},
    {'id': 4, 'name': 'Titanic', 'price': 11,
     'description': 'A love story set against the backdrop of the sinking Titanic.'},
]


def index(request):
    template_data = {'title': 'Movies', 'movies': movies}
    return render(request, 'movies/index.html', {'template_data': template_data})


def show(request, id):
    movie = next((m for m in movies if m["id"] == id), None)
    if not movie:
        return render(request, 'movies/index.html', {'error': 'Movie not found'})

    template_data = {'title': movie['name'], 'movie': movie}
    return render(request, 'movies/show.html', {'template_data': template_data})

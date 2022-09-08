from django.shortcuts import render
from .models import Author, Movie, MovieInstance
from django.views import generic

# Create your views here.

def index(request):
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    available = MovieInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'num_authors': num_authors,
            'num_instances': num_instances,
            'available': available,
        }
    )

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 10

class MovieDetailView(generic.DetailView):
    model = Movie

class AuthorListView(generic.ListView):
    model= Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model=Author


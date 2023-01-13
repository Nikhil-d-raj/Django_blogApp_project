from django.shortcuts import render
from blog.models import Post, Movie
from django.contrib.auth.forms import UserCreationForm
from blog.forms import CreateUserForm
def frontpage(request):
    posts = Post.objects.all()

    return render(request, "core/frontpage.html", {'posts': posts })
def about(request):
    
    return render(request, "core/about.html")
def movie(request):
    movies = Movie.objects.all()
    return render(request, "core/movie.html", {'movies': movies})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "core/register.html", context)

def login(request):
    context = {}
    return render(request, "core/login.html", context)


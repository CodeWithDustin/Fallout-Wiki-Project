from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from app.forms import *
from app.models import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    user = request.user  # Get the current logged-in user
    context = {'user': user}
    return render(request, 'profile.html', context)

#Check if user is an admin
def is_admin(user):
    return user.is_staff

# List views
def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles_list.html', {'articles': articles})

def characters_list(request):
    characters = Character.objects.all()
    return render(request, 'characters_list.html', {'characters': characters})

def locations_list(request):
    locations = Location.objects.all()
    return render(request, 'locations_list.html', {'locations': locations})

# Detail views
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'character_detail.html', {'character': character})

def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'location_detail.html', {'location': location})

# add new game to form list
def add_game(request):
    if request.method == 'POST':
        form = GameAddForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    else:
        form = GameAddForm()
    return render(request, 'add_game.html', {'game_form': form})

#remove game from list
@login_required
def remove_game(request):
    if not request.user.is_superuser:
        return render(request, 'access_denied.html')

    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        game = get_object_or_404(Game, id=game_id)
        game.delete()
        return redirect('remove_game')

    games = Game.objects.all()
    return render(request, 'remove_game.html', {'games': games})

# Create views
@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles_list')
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})

@login_required
def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.author = request.user
            character.save()
            return redirect('characters_list')
    else:
        form = CharacterForm()
    return render(request, 'character_form.html', {'form': form})

@login_required
def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.author = request.user
            location.save()
            return redirect('locations_list')
    else:
        form = LocationForm()
    return render(request, 'location_form.html', {'form': form})

# Update views
@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})

@login_required
def character_update(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_detail', pk=pk)
    else:
        form = CharacterForm(instance=character)
    return render(request, 'character_form.html', {'form': form})

@login_required
def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_detail', pk=pk)
    else:
        form = LocationForm(instance=location)
    return render(request, 'location_form.html', {'form': form})

# Delete views
@user_passes_test(is_admin)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles_list')
    return render(request, 'article_confirm_delete.html', {'article': article})

@user_passes_test(is_admin)
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('characters_list')
    return render(request, 'character_confirm_delete.html', {'character': character})

@user_passes_test(is_admin)
def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('locations_list')
    return render(request, 'location_confirm_delete.html', {'location': location})

# Search view
def search(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query)
    characters = Character.objects.filter(name__icontains=query)
    locations = Location.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {
        'articles': articles,
        'characters': characters,
        'locations': locations
    })



"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('articles/', articles_list, name='articles_list'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('articles/create/', article_create, name='article_create'),
    path('articles/<int:pk>/update/', article_update, name='article_update'),
    path('articles/<int:pk>/delete/', article_delete, name='article_delete'),
    path('characters/', characters_list, name='characters_list'),
    path('characters/<int:pk>/', character_detail, name='character_detail'),
    path('characters/create/', character_create, name='character_create'),
    path('characters/<int:pk>/update/', character_update, name='character_update'),
    path('characters/<int:pk>/delete/', character_delete, name='character_delete'),
    path('locations/', locations_list, name='locations_list'),
    path('locations/<int:pk>/', location_detail, name='location_detail'),
    path('locations/create/', location_create, name='location_create'),
    path('locations/<int:pk>/update/', location_update, name='location_update'),
    path('locations/<int:pk>/delete/', location_delete, name='location_delete'),
    path('add-game/', add_game, name='add_game'),
    path('remove_game/', remove_game, name='remove_game'),
    path('search/', search, name='search'),
    path('profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
]

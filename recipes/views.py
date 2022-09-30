from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from utils.factory import make_recipe
# Create your views here.

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_descripit_block': True,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_descripit_block': True,
})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datail_page': True,
    })
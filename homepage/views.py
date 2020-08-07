from django.shortcuts import render
from homepage.models import Recipe, Author

# Create your views here.

def recipe_list(request):
    my_recipes = Recipe.objects.all()
    return render(request, 'list_view.html', {'recipes': my_recipes, 'home': 'List of Recipes'})

def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'rec_detail.html', { 'recipe': my_recipe })

def author_detail(request, author_name):
    recipes = Recipe.objects.all()
    selected_author = Author.objects.filter(name=author_name).first()
    return render(request, 'auth_detail.html', { 'author': selected_author, 'recipes': recipes })
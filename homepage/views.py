from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm

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

def recipe_form(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                time_required=data.get('time_required'),
                description=data.get('description'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeForm()

    return render(request, "generic_form.html", {'form': form})

def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorForm()
    return render(request, 'generic_form.html', {'form': form})

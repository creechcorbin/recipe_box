from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm, LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def recipe_list(request):
    my_recipes = Recipe.objects.all()
    user = request.user
    return render(request, 'list_view.html', {'recipes': my_recipes, 'home': 'List of Recipes', 'user': user})

def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'rec_detail.html', { 'recipe': my_recipe })

def author_detail(request, author_name):
    recipes = Recipe.objects.all()
    selected_author = Author.objects.filter(name=author_name).first()
    return render(request, 'auth_detail.html', { 'author': selected_author, 'recipes': recipes })

@login_required
def recipe_form(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=request.user.author,
                time_required=data.get('time_required'),
                description=data.get('description'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeForm()

    return render(request, "generic_form.html", {'form': form})

@login_required
def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    if request.user.is_staff:
        form = AuthorForm()
        return render(request, 'generic_form.html', {'form': form})
    else:
        return render(request, 'error.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
            Author.objects.create(name=data.get('username'), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
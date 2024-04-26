from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm

## Create your views here.
def homepage(request):
    return render(request, 'main/homepage.html')

def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'main/recipes.html', {'recipes': recipes})

def write_a_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Assign the logged-in user as the author of the recipe
                author = request.user
            else:
                # If the user is not logged in, set the author to "Anonymous"
                author = None  # Or None
            # Save the recipe with the appropriate author
            recipe = form.save(commit=False)
            recipe.author = author
            recipe.save()
            return redirect(reverse('main:recipes'))  # Redirect to a page displaying a list of recipes
    else:
        form = RecipeForm()
    return render(request, 'main/write_a_recipe.html', {'form': form})
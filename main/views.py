from django.shortcuts import render, redirect

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
            form.save()
            return redirect('recipe_list')  # Redirect to a page displaying a list of recipes
    else:
        form = RecipeForm()
    return render(request, 'main/write_a_recipe.html', {'form': form})
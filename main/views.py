from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm

## Create your views here.
def homepage(request):
    return render(request, 'main/homepage.html')

from django.shortcuts import render
from .models import Recipe

def all_recipes(request):
    all_recipes = Recipe.objects.all()
    all_equipment = Recipe.objects.exclude(equipment=None).values_list('equipment__name', flat=True).distinct()
    all_ingredients = Recipe.objects.exclude(ingredients=None).values_list('ingredients__name', flat=True).distinct()
    
    search_query = request.GET.get('search_query', '')
    equipment = request.GET.getlist('equipment', [])
    ingredients = request.GET.getlist('ingredients', [])
    category = request.GET.get('category', '')  # Get the category parameter from the URL query string
    
    filtered_recipes = all_recipes
    
    if search_query:
        filtered_recipes = filtered_recipes.filter(name__icontains=search_query)
    if equipment:
        filtered_recipes = filtered_recipes.filter(equipment__name__in=equipment)
    if ingredients:
        filtered_recipes = filtered_recipes.filter(ingredients__name__in=ingredients)
    if category:  # If category parameter is provided, filter by category
        filtered_recipes = filtered_recipes.filter(category=category)

    context = {
        'filtered_recipes': filtered_recipes,
        'all_equipment': all_equipment,
        'all_ingredients': all_ingredients
    }
    return render(request, 'main/all_recipes.html', context)

def user_recipes(request):
    if request.user.is_authenticated:
        user_recipes = Recipe.objects.filter(author=request.user)
    else:
        user_recipes = Recipe.objects.none()

    search_query = request.GET.get('search_query', '')
    category = request.GET.get('category', '')  # Get the category parameter from the URL query string

    # Apply filters
    if search_query:
        user_recipes = user_recipes.filter(name__icontains=search_query)
    if category:  # If category parameter is provided, filter by category
        user_recipes = user_recipes.filter(category=category)

    context = {
        'filtered_recipes': user_recipes,
    }
    return render(request, 'main/user_recipes.html', context)


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
            return redirect(reverse('main:user_recipes'))  # Redirect to a page displaying a list of the users' recipes
    else:
        form = RecipeForm()
    return render(request, 'main/write_a_recipe.html', {'form': form})
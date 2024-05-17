from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm

## Create your views here.
def saved_recipes(request):
    saved_recipes = Recipe.objects.all() # DODATI OGRANIČENJE!!!
    search_query = request.GET.get('search_query', '')
    category = request.GET.get('category', '')  # Get the category parameter from the URL query string
    
    filtered_recipes = saved_recipes
    
    if search_query:
        filtered_recipes = filtered_recipes.filter(name__icontains=search_query)
    if category:  # If category parameter is provided, filter by category
        filtered_recipes = filtered_recipes.filter(category=category)

    context = {
        'filtered_recipes': filtered_recipes
    }
    return render(request, 'main/saved_recipes.html', context)

def all_recipes(request):
    all_recipes = Recipe.objects.all()
    search_query = request.GET.get('search_query', '')
    category = request.GET.get('category', '')  # Get the category parameter from the URL query string
    
    filtered_recipes = all_recipes
    
    if search_query:
        filtered_recipes = filtered_recipes.filter(name__icontains=search_query)
    if category:  # If category parameter is provided, filter by category
        filtered_recipes = filtered_recipes.filter(category=category)

    context = {
        'filtered_recipes': filtered_recipes
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

def user_edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('main:user_recipes')
    else:
        form = RecipeForm(instance=recipe)
    
    context = {
        'form': form,
    }
    return render(request, 'main/user_edit_recipe.html', context)

def user_delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    recipe.delete()
    return redirect('main:user_recipes')

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

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'main/recipe.html', {'recipe': recipe})
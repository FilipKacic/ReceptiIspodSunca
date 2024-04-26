from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from django import forms
from .models import Recipe

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('main:homepage')  # Assuming 'homepage' is the name of your homepage URL pattern
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'equipment', 'ingredients', 'time_needed', 'preperation']
        labels = {
            'name': 'Naziv', 
            'equipment': 'Oprema', 
            'ingredients': 'Sastojci', 
            'time_needed': 'Potrebno vrijeme za pripremu',
            'preperation': 'Priprema'
        }
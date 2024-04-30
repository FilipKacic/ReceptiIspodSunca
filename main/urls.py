from django.urls import path
from . import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('all_recipes', views.all_recipes, name='all_recipes'),
    path('user_recipes', views.user_recipes, name='user_recipes'),
    path('edit_recipe/<int:recipe_id>/', user_edit_recipe, name='user_edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', user_delete_recipe, name='user_delete_recipe'),
    path('write_a_recipe', views.write_a_recipe, name='write_a_recipe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
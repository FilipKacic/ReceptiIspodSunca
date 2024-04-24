from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('recipes', views.recipes, name='recipes'),
    path('write_a_recipe', views.write_a_recipe, name='write_a_recipe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
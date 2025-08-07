# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    # Detalhe da receita pelo ID
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    # Outras URLs do seu aplicativo podem ser adicionadas aqui
]
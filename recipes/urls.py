from django.urls import path
from recipes import views

urlpatterns = [
    path('recipes/', views.RecipeListCreateView.as_view(), name = 'recipe-list-create'),
    path('recipes/<int:pk>/', views.RecipeRetriveUpdateDestroyView.as_view(), name = 'recipe-detail'),
]

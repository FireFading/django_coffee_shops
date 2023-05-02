from django.urls import path
from recipes.views import CreateRecipeView, RecipeDetailView, RecipesListView

app_name = "recipes"

urlpatterns = [
    path("", RecipesListView.as_view(), name="all"),
    path("<str:recipe_name>/", RecipeDetailView.as_view(), name="detail"),
    path("new/", CreateRecipeView.as_view(), name="new"),
]

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from recipes.filters import RecipeFilter
from recipes.models import Recipe


class RecipesListView(ListView):
    model = Recipe
    template_name = "recipes/all.html"
    context_object_name = "recipes"
    paginate_by = 50

    def get_queryset(self):
        self.filterset = queryset = RecipeFilter(self.request.GET, queryset=Recipe.objects.filter())
        return queryset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"
    slug_field = "name"
    slug_url_kwarg = "recipe_name"
    context_object_name = "recipe"


class CreateRecipeView(CreateView):
    model = Recipe
    fields = "__all__"
    template_name = "recipes/add_new.html"
    success_url = reverse_lazy("menu:catalog")

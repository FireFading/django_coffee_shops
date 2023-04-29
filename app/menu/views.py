from django.views.generic import DetailView, ListView, TemplateView
from menu.filters import MenuFilter
from menu.models import MenuItem


class HomeView(TemplateView):
    template_name = "base/home.html"


class ProductsListView(ListView):
    model = MenuItem
    template_name = "menu/all.html"
    context_object_name = "products"
    paginate_by = 50

    def get_queryset(self):
        self.filterset = queryset = MenuFilter(self.request.GET, queryset=MenuItem.objects.filter())
        return queryset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context


class ProductDetailView(DetailView):
    model = MenuItem
    template_name = "menu/detail.html"
    slug_field = "name"
    slug_url_kwarg = "product_name"
    context_object_name = "product"

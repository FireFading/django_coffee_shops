from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from menu.filters import MenuFilter
from menu.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = "menu/all.html"
    context_object_name = "products"
    paginate_by = 50

    def get_queryset(self):
        self.filterset = queryset = MenuFilter(self.request.GET, queryset=Product.objects.filter())
        return queryset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "menu/detail.html"
    slug_field = "name"
    slug_url_kwarg = "product_name"
    context_object_name = "product"


class CreateProductView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "menu/add_new.html"
    success_url = reverse_lazy("menu:catalog")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["price", "description", "shop"]
    template_name = "menu/edit.html"

    def get_object(self, queryset=None):
        product_name = self.kwargs.get("product_name")
        return get_object_or_404(Product, name=product_name)

    def get_success_url(self):
        return reverse("menu:detail", kwargs={"product_name": self.object.name})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "menu/delete.html"
    success_url = reverse_lazy("menu:catalog")

    def get_object(self, queryset=None):
        product_name = self.kwargs.get("product_name")
        return get_object_or_404(Product, name=product_name)


class AddToFavoritesView(View):
    def post(self, request, *args, **kwargs):
        product_name = kwargs.get("product_name")
        menu_item = get_object_or_404(Product, name=product_name)

        request.user.favorites.add(menu_item)

        return redirect("menu:detail", product_name=product_name)


class RemoveFromFavoritesView(View):
    def post(self, request, *args, **kwargs):
        product_name = kwargs.get("product_name")
        menu_item = get_object_or_404(Product, name=product_name)

        request.user.favorites.remove(menu_item)

        return redirect("menu:detail", product_name=product_name)

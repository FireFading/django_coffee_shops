from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from menu.filters import MenuFilter
from django.shortcuts import get_object_or_404
from menu.models import MenuItem
from django.urls import reverse


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


class CreateProductView(CreateView):
    model = MenuItem
    fields = "__all__"
    template_name = "menu/add_new.html"
    success_url = reverse_lazy("menu:catalog")


class ProductUpdateView(UpdateView):
    model = MenuItem
    fields = ['price', "description", "shop"]
    template_name = 'menu/edit.html'

    def get_object(self, queryset=None):
        product_name = self.kwargs.get('product_name')
        return get_object_or_404(MenuItem, name=product_name)

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'product_name': self.object.name})


class ProductDeleteView(DeleteView):
    model = MenuItem
    template_name = 'menu/delete.html'
    success_url = reverse_lazy('menu:catalog')

    def get_object(self, queryset=None):
        product_name = self.kwargs.get('product_name')
        return get_object_or_404(MenuItem, name=product_name)
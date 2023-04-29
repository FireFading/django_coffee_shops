from django.views.generic import DetailView, ListView
from shops.filters import ShopFilter
from shops.models import Shop


class ShopsListView(ListView):
    model = Shop
    template_name = "shops/all.html"
    context_object_name = "shops"
    paginate_by = 50

    def get_queryset(self):
        self.filterset = queryset = ShopFilter(self.request.GET, queryset=Shop.objects.filter())
        return queryset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context


class ShopDetailView(DetailView):
    model = Shop
    template_name = "shops/detail.html"
    slug_field = "name"
    slug_url_kwarg = "shop_name"
    context_object_name = "shop"

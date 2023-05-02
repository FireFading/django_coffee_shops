from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from shops.filters import ShopFilter
from shops.models import Shop
from django.urls import reverse


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


class CreateShopView(CreateView):
    model = Shop
    fields = "__all__"
    template_name = "shops/add_new.html"
    success_url = reverse_lazy("shops:all")


class ShopUpdateView(UpdateView):
    model = Shop
    fields = ['address', "phone_number", "opening_time", "closing_time"]
    template_name = 'shops/edit.html'

    def get_object(self, queryset=None):
        shop_name = self.kwargs.get('shop_name')
        return get_object_or_404(Shop, name=shop_name)

    def get_success_url(self):
        return reverse('shops:detail', kwargs={'shop_name': self.object.name})

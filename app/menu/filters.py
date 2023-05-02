from django_filters import CharFilter, FilterSet, ModelChoiceFilter, NumberFilter, OrderingFilter
from menu.models import Category, Product
from shops.models import Shop


class MenuFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    price_from = NumberFilter(field_name="price", lookup_expr="gt")
    price_to = NumberFilter(field_name="price", lookup_expr="lt")
    ordering = OrderingFilter(
        fields=(
            ("name", "name"),
            ("price", "price"),
        ),
        field_labels={"name": "By name", "price": "By price"},
    )

    shop = ModelChoiceFilter(field_name="shop", queryset=Shop.objects.all(), to_field_name="name")
    category = ModelChoiceFilter(field_name="category", queryset=Category.objects.all(), to_field_name="name")

    def filter_available(self, queryset, name, value):
        lookup = "__".join([name, "isnull"])
        return queryset.filter(**{lookup: False})

    class Meta:
        model = Product
        fields = ["name", "shop"]

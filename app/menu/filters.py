from django_filters import CharFilter, FilterSet, ModelChoiceFilter, NumberFilter, OrderingFilter
from menu.models import MenuItem
from shops.models import Shop


class MenuFilter(FilterSet):
    name = CharFilter(field_name="Название", lookup_expr="icontains")
    price_from = NumberFilter(field_name="Цена от", lookup_expr="gt")
    price_to = NumberFilter(field_name="Цена до", lookup_expr="lt")
    ordering = OrderingFilter(
        fields=(
            ("name", "name"),
            ("price", "price"),
        ),
        field_labels={"name": "По названию", "price": "По цене"},
    )

    shop = ModelChoiceFilter(field_name="shop", queryset=Shop.objects.all(), to_field_name="name")

    def filter_available(self, queryset, name, value):
        lookup = "__".join([name, "isnull"])
        return queryset.filter(**{lookup: False})

    class Meta:
        model = MenuItem
        fields = ["name", "shop"]

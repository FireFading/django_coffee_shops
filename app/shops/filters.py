from django_filters import CharFilter, FilterSet, OrderingFilter
from shops.models import Shop


class ShopFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    address = CharFilter(field_name="address", lookup_expr="icontains")
    ordering = OrderingFilter(
        fields=(
            ("name", "name"),
            ("address", "address"),
        ),
        field_labels={"name": "По названию", "address": "По адресу"},
    )

    class Meta:
        model = Shop
        fields = ["name", "address"]

from django_filters import CharFilter, FilterSet, ModelChoiceFilter, OrderingFilter
from menu.models import Product
from users.models import User


class RecipeFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    products = ModelChoiceFilter(field_name="products", queryset=Product.objects.all(), to_field_name="name")
    user = ModelChoiceFilter(field_name="user", queryset=User.objects.all(), to_field_name="email")
    ordering = OrderingFilter(
        fields=(
            ("name", "name"),
            ("created_at", "created_at"),
        ),
        field_labels={"name": "By name", "created_at": "By time"},
    )

    def filter_available(self, queryset, name, value):
        lookup = "__".join([name, "isnull"])
        return queryset.filter(**{lookup: False})

    class Meta:
        model = Product
        fields = ["name", "products",]

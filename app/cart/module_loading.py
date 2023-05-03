from importlib import import_module

from django.conf import settings


def get_product_model():
    """
    Returns the product model that is used by this cart.
    """
    package, module = settings.CART_PRODUCT_MODEL.rsplit(".", 1)
    return getattr(import_module(package), module)

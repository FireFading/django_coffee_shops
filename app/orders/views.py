from cart.main import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from menu.models import Product
from orders.models import Order, OrderItem
from orders.tasks import send_mail_confirm_order, send_mail_order_to_admin


class CartView(TemplateView):
    template_name = "cart/summary.html"


def add_product(request, product_id, next):
    if request.method == "POST":
        cart = Cart(request.session)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, price=product.price)
    request.session.modified = True
    return redirect(next)


def remove_product(request, product_id, next):
    if request.method == "POST":
        cart = Cart(request.session)
        product = get_object_or_404(Product, id=product_id)
        cart.remove_single(product)
    request.session.modified = True
    return redirect(next)


def remove_products(request, product_id, next):
    if request.method == "POST":
        cart = Cart(request.session)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
    request.session.modified = True
    return redirect(next)


@login_required(login_url="users:login")
def create_order(request):
    if request.method == "POST":
        user = request.user
        message = request.GET.get("comment")
        cart = Cart(request.session)
        if cart.count > 0:
            order = Order.objects.create(user=user, message=message)
            total_price = 0
            for item in cart.items:
                product = Product.objects.get(pk=item.product.id)
                quantity = item.quantity
                total_price += round((quantity * product.price), 2)
                OrderItem.objects.create(
                    order=order,
                    product=product.name,
                    quantity=quantity,
                )
            order.total_price = total_price
            order.save()
            cart.clear()
            request.session.modified = True
            send_mail_confirm_order(order=order, request=request)
            send_mail_order_to_admin(order=order)
            messages.success(request, "Order successfully created")

    return redirect("orders:cart")

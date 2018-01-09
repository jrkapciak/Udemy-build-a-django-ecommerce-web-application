from django.shortcuts import render, redirect

from .models import Cart
from products.models import Product


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {'cart':cart_obj}
    return render(request, 'carts/home.html',context)


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('cart:home')
        cart, new_obj = Cart.objects.new_or_get(request)
        if product in cart.products.all():
            cart.products.remove(product)
        else:
            cart.products.add(product)
        request.session['cart_item'] = cart.products.count()
    return redirect("cart:home")

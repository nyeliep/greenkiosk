from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartForm
from .models import Cart
from .models import CartItem
from .models import Product
from  order.models import Order




def cart_list(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart_list.html', {'cart_items': cart_items})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})


def edit_cart(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    if request.method == 'POST':
        form = CartForm(request.POST, request.FILES, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm(instance=cart)
        return render(request, 'edit_cart.html', {'form': form, 'cart': cart})


def create_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect('cart_list')
    else:
        form = CartForm()
        return render(request, 'cart/create_cart.html', {'form': form})




def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    return render(request, 'cart_detail.html', {'cart': cart})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = CartItem.objects.get(user=request.user, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(user=request.user, product=product, quantity=1)

    return redirect('cart_list')



def remove_product_view(request, cart_id, product_id):
    cart = get_object_or_404(Cart, id=cart_id)
    product = get_object_or_404(Product, id=product_id)
    cart.products.remove(product)
    return redirect('cart_detail.html')


def checkout_view(request, basket_id):
    cart = get_object_or_404(Cart, id=basket_id)
    order = Order.objects.create(cart=cart, user=request.user)
    cart.clear()
    return render(request, 'cart/checkout_confirmation.html', {'order': order})











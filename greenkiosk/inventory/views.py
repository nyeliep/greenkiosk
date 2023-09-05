from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductUploadForm
from  cart.models import CartItem
from .models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_list')



def product_upload_view(request):
    if request.method=="POST":
       form = ProductUploadForm(request.POST)
       if form.is_valid():
           form.save()
    else:
       form=ProductUploadForm()

       return render(request,"inventory/product_upload.html",{"form":form})


def product_list(request):
    products = Product.objects.all()
    return render(request,"inventory/product_list.html",{"products":products})

def product_detail(request,id):
    product= Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html",{"product":product})


def product_update_view(request, id):
    product = Product.objects.get(id=id)

    form = ProductUploadForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_update_view', id=id)
    else:
        context = {
            'form': form,
        }
        return render(request, 'inventory/edit_product.html', context)
        
def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product-list')
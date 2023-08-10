from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from .models import Product
from django.shortcuts import render


# Create your views here.
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
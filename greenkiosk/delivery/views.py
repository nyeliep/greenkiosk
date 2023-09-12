from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeliveryForm
from .models import Delivery
from  order.models import  Order

def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm()
    return render(request, 'delivery/create_delivery.html', {'form': form})

def edit_delivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, 'delivery/edit_delivery.html', {'form': form, 'delivery': delivery})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliveries': deliveries})

def delivery_detail(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    return render(request, 'delivery/delivery_detail.html', {'delivery': delivery})



def delivery_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':

        delivery = Delivery.objects.create(order=order, tracking_number='123456', status='delivered')

        order.status = 'delivered'
        order.save()
        return redirect('delivery_confirmation_view')

    return render(request, 'delivery_form.html', {'order': order})


def delivery_confirmation_view(request):
    latest_delivery = Delivery.objects.latest('delivery_date')
    context = {
        'message': "Your delivery has been confirmed.",
        'delivery_date': latest_delivery.delivery_date,
        'tracking_number': latest_delivery.tracking_number,
    }

    return render(request, 'delivery/delivery_confirmation.html', context)


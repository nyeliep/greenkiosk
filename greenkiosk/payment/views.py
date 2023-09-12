from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Payment
from  order.models import Order

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment/create_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payments': payments})




def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        payment = Payment.objects.create(order=order, amount=order.total_amount, payment_method='Credit Card')

        order.status = 'Paid'
        order.save()

        return redirect('payment_confirmation_view')

    return render(request, 'payment_form.html', {'order': order})



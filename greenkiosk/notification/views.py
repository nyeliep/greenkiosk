from django.shortcuts import render, redirect
from .forms import NotificationForm
from .models import Notification

def create_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm()
    return render(request, 'notification/create_notification.html', {'form': form})

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notification/notification_list.html', {'notifications': notifications})


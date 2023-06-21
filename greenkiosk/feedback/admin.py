from django.contrib import admin

# Register your models here.
from .models import Feedback
class Feedback_admin(admin.ModelAdmin):
    list_display = ("feedback", "date", "ratings")
admin.site.register(Feedback,Feedback_admin)
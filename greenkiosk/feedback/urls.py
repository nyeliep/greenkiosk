from django.urls import path
from .views import create_feedback, feedback_list

urlpatterns = [
    path('feedbacks/create/', create_feedback, name='create_feedback'),
    path('feedbacks/', feedback_list, name='feedback_list'),
]

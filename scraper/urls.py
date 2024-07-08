from django.urls import path
from .views import algorithm_list

urlpatterns = [
    path('', algorithm_list, name='algorithm_list'),
]

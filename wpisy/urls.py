
from django.urls import path
from wpisy import views

urlpatterns = [

    path('', views.wpisy_list),
]
from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage , name='home'),
    path('contactus/', views.contact , name='contact')
]
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home),
    path('login/',views.login),
    path('contacto/',views.contacto),
    path('producto/',views.producto),
    path('seguimiento/',views.seguimiento),
]

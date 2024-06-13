from django.urls import path
from . import views

urlpatterns = [ 
    path('log_emp/', views.login_emp),
    path('administrator/',views.administrador),
    path('contador/',views.contador),
    path('bodega/',views.bodega),
    path('vendedor/',views.vendedor), 
    
]

from django.shortcuts import render

def login_emp(request):
    return render(request, 'login_emp.html')

def administrador(request):
    return render(request, 'admin.html')

def contador(request):
    return render(request, 'contador.html')

def bodega(request):
    return render(request, 'bodeguero.html')

def vendedor(request):
    return render(request, 'vendedor.html')







# Create your views here.

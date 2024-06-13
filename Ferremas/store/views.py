from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contacto(request):
    return render(request, 'cantacto.html')

def producto(request):
    return render(request, 'producto.html')

def seguimiento(request):
    return render(request, 'seguimiento.html')

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html')

def peliculas(request):
    return render(request, 'miapp/peliculas.html')

def nombres(request):
    return render(request, 'miapp/nombres.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
 return render(request, 'galeria/index.html')

def livros(request):
 return render(request, 'galeria/livros_lidos.html')

def estatisticas(request):  
 return render(request, 'galeria/estatisticas.html')

def saiba_mais(request):    
 return render(request, 'galeria/saiba_mais.html')

def login(request):    
 return render(request, 'galeria/login.html')
 



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Adicione um nome para facilitar referências
    path('livros_lidos/', views.livros, name='livros_lidos'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    path('saiba_mais/', views.saiba_mais, name='saiba_mais'),
    path('login/', views.login, name='login'),
    
]

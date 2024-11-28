
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Adicione um nome para facilitar referências
]

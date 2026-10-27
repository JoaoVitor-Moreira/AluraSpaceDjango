from django.urls import path
from galeria.views import index, imagem, buscar, buscar_aleatorio

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('surpreendame', buscar_aleatorio, name='surpreendame')
]
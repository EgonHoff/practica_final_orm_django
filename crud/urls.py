from django.urls import path
from .views import insertar_lab, mostrar_lab, eliminar_lab, editar_lab, actualizarlab

urlpatterns = [
    path('mostrar/', mostrar_lab, name='mostrar_lab'),
    path('insertar/', insertar_lab, name='insertar_lab'),
    path('editar/<int:pk>', editar_lab, name='editar_lab'),
    path('editar/actualizarlab/<int:id>', actualizarlab, name='actualizar_lab'),
    path('eliminar/<int:pk>', eliminar_lab, name='eliminar_lab'),
]
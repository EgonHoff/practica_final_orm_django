from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.

### Creamos la vista en el sitio de django admin ref: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',)
    ordering = ('id',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',
                    'laboratorio',)
    ordering = ('id',)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',
                    'laboratorio',
                    'f_fabricacion_y',
                    'p_costo',
                    'p_venta',)
    list_select_related = ['laboratorio']

    list_filter = ('nombre',
                   'laboratorio',)
    ordering = ('id',)

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
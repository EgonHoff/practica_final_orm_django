# practica_final_orm_django

## CONSOLIDACION M7

Estado inicial del proyecto

## Tecnologias utilizadas

- Vs-code
- GoogleChrome
- Python 3.12.4

## Creación del Entorno virtual con VirtualEnvwrapper

- Nombre entorno : practica_final_orm_django
- Revisar requeriments.txt y env_log.txt para mas información

## Creacion base de Datos

- Configuracion de postgresql en setting.py
- Crear base de datos db_final_orm
- Realizar migraciones correspondientes

## Cambio a la branch Develop

- git checkout -b develop
- git push -u origin develop

## Creacion del Modelo laboratorio

- laboratorio\models.py
### Modelos

- Laboratorio:
    - nombre: cadena de caracteres. 

- DirectorGeneral:
    - nombre: cadena de caracteres.
    - laboratorio: Laboratorio.

- Producto:
    - nombre: cadena de caracteres.
    - laboratorio: Laboratorio.
    - f_fabricacion: Tipo fecha que comienza desde el 2015.
    - p_costo: decimal con 2 dígitos decimales, y 10 dígitos en la parte entera.
    - p_venta: decimal con 2 dígitos decimales, y 10 dígitos en la parte entera.

### Constrains

- Laboratorio - Director General es One to One Field
- Laboratorio - Producto Many to one Field

## Adecuando la Interfaz administrativa del sitio de Django

### Para incluir los modelos en el sitio

- laboratorio\admin.py
```{pythopn}
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
```

### Para adecuar para que se observe la tabla como se indica

- laboratorio\admin.py
```{python}
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',
                    'laboratorio',)
    
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
```
Se utiliza la clase ModelAdmin para agregar a la vista todos los atributos y el filtro requerido.

## Consultas a la base de Datos en shell

- py manage.py shell
- Se importan los modelos
```{python}
from laboratorio.models import Laboratorio, DirectorGeneral, Producto
```

### Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.

```{python}
laboratorios = Laboratorio.objects.all()
print(list(laboratorios))

[<Laboratorio: Laboratorio1>, <Laboratorio: Laboratorio2>, <Laboratorio: Laboratorio3>]

directores_generales = DirectorGeneral.objects.all()
print(list(directores_generales))

[<DirectorGeneral: Director General 1>, <DirectorGeneral: Director General 2>, <DirectorGeneral: Director General 3>]

productos = Producto.objects.all()
print(list(productos))

[<Producto: Producto 1>, <Producto: Producto 3>, <Producto: Producto 2>]
```

### Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.

```{python}
producto_1 = Producto.objects.get(nombre='Producto 1')
print(producto_1.laboratorio.nombre)

Laboratorio1
```

### Ordene  todos  los  productos  por  nombre,  y  que  muestre  los  valores  de  nombre  y laboratorio.

```{python}
productos_ordenados = Producto.objects.order_by('nombre')
for producto in productos_ordenados:
    print(f'Producto: {producto.nombre} Laboratorio: {producto.laboratorio.nombre}')

Producto: Producto 1 Laboratorio: Laboratorio1
Producto: Producto 2 Laboratorio: Laboratorio2
Producto: Producto 3 Laboratorio: Laboratorio3
```

### Realice una consulta que imprima por pantalla los laboratorios de todos los productos.

```{python}
for producto in Producto.objects.all():
    print(f'Producto: {producto.nombre} Laboratorio: {producto.laboratorio.nombre}')

Producto: Producto 1 Laboratorio: Laboratorio1
Producto: Producto 3 Laboratorio: Laboratorio3
Producto: Producto 2 Laboratorio: Laboratorio2
```


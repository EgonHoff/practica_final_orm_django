from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

### Crearemos un validador para la fecha de fabricacion ref : https://docs.djangoproject.com/en/5.1/ref/validators/

def date_value_validator(value):
    if value.year <= 2014:
        raise ValidationError('La fecha debe ser 2015 o mayor')

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Laboratorio'

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Director General'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[date_value_validator])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'Productos'

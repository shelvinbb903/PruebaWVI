from django.db import models

class ContactoModel(models.Model):
    cedula = models.CharField(primary_key=True, max_length=50)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    estado = models.BooleanField()
    usuario = models.CharField(max_length=50)
    Fecha = models.DateTimeField()
        
    class Meta:
        db_table = 'TblContacto'
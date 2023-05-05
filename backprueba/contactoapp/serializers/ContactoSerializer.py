from contactoapp.models import ContactoModel
from rest_framework import serializers

class ContactosSerializer(serializers.Serializer):
    cedula = serializers.CharField(max_length=50, required=False)
    nombres = serializers.CharField(max_length=50, required=False)
    apellidos = serializers.CharField(max_length=50, required=False)
    telefono = serializers.IntegerField(required=False)
    correo = serializers.CharField(max_length=50, required=False)
    ocupacion = serializers.CharField(max_length=50, required=False)
    estado = serializers.BooleanField(required=False)
    usuario = serializers.CharField(max_length=50, required=False)
    Fecha = serializers.DateTimeField(required=False)

    """ Validar existencia del numero de cedula """
    def validate_cedula(self, value):
        contacto_data = ContactoModel.objects.filter(cedula=value)
            
        if contacto_data.__len__() > 0:                
            raise serializers.ValidationError("Cedula ya existe")
        
        return value
    
    def create(self, validated_data):
        contacto = ContactoModel.objects.create(**validated_data)
        return contacto 
    
    class Meta:
        model = ContactoModel
        fields = ['cedula', 'nombres', 'apellidos', 'telefono', 'correo', 'ocupacion', 'estado', 'usuario', 'Fecha']

class ListContactosSerializer(serializers.Serializer):
    cedula = serializers.CharField(max_length=50)
    nombres = serializers.CharField(max_length=50)
    apellidos = serializers.CharField(max_length=50)
    telefono = serializers.IntegerField()
    correo = serializers.CharField(max_length=50)
    ocupacion = serializers.CharField(max_length=50)
    estado = serializers.BooleanField()
    usuario = serializers.CharField(max_length=50)
    Fecha = serializers.DateTimeField()
    
    class Meta:
        model = ContactoModel
        fields = ['cedula', 'nombres', 'apellidos', 'telefono', 'correo', 'ocupacion', 'estado', 'usuario', 'Fecha']
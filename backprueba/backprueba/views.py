from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from contactoapp.models import ContactoModel
from contactoapp.serializers.ContactoSerializer import ListContactosSerializer, ContactosSerializer
from datetime import datetime

# Create your views here.
class ContactoAPPView(APIView):
    """ Creacion de contactos """
    def post(self, request):
        response = dict()
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
        
        data["usuario"] = "prueba";
        data["Fecha"] = datetime.today();
        serializer = ContactosSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            contacto = serializer.create(serializer.data)
            serializer_data = ListContactosSerializer(contacto, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 
    
    """ Lista de contactos registrados
        Se puede listar todos los registros o se puede filtrar la consulta 
        por los campos en la tabla
    """
    def get(self, request):
        response = dict()
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}            
        
        queryset = ContactoModel.objects.filter(**data)
        serializer = ListContactosSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
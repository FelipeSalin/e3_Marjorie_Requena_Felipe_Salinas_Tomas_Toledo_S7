from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from Inicio.models import TipoUsuario, Usuario, Comuna, Region, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle 
from .serializers import TipoUsuarioSerializer, UsuarioSerializer, ComunaSerializer, RegionSerializer, MarcaSerializer, ModeloSerializer, ProductoSerializer, DetalleSerializer, DireccionSerializer, VentaSerializer, CategoriaSerializer, TipoProdSerializer

# Create your views here.

#Listas de los modelos (GET, POST)

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_TipoUsuario(request):
    if request.method == 'GET':
        tipoUsuario = TipoUsuario.objects.all()
        serializer = TipoUsuarioSerializer(tipoUsuario, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TipoUsuarioSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Usuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Comuna(request):
    if request.method == 'GET':
        comuna = Comuna.objects.all()
        serializer = ComunaSerializer(comuna, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComunaSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Region(request):
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Direccion(request):
    if request.method == 'GET':
        direccion = Direccion.objects.all()
        serializer = DireccionSerializer(direccion, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DireccionSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Venta(request):
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_TipoProd(request):
    if request.method == 'GET':
        tipoProd = TipoProd.objects.all()
        serializer = TipoProdSerializer(tipoProd, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TipoProdSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Marca(request):
    if request.method == 'GET':
        marca = Marca.objects.all()
        serializer = MarcaSerializer(marca, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Modelo(request):
    if request.method == 'GET':
        modelo = Modelo.objects.all()
        serializer = ModeloSerializer(modelo, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ModeloSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Producto(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_Detalle(request):
    if request.method == 'GET':
        detalle = Detalle.objects.all()
        serializer = DetalleSerializer(detalle, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetalleSerializer(data = data) #revisar BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

#Detalles de los modelos (GET, PUT, DELETE)
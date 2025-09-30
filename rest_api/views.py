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

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_TipoUsuario(request, id):
    try:
        m = TipoUsuario.objects.get(id = id) #ver BD
    except TipoUsuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TipoUsuarioSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TipoUsuarioSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Usuario(request, id):
    try:
        m = Usuario.objects.get(id = id) #ver BD
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Comuna(request, id):
    try:
        m = Comuna.objects.get(id = id) #ver BD
    except Comuna.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ComunaSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ComunaSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Region(request, id):
    try:
        m = Region.objects.get(id = id) #ver BD
    except Region.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RegionSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Direccion(request, id):
    try:
        m = Direccion.objects.get(id = id) #ver BD
    except Direccion.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DireccionSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DireccionSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Venta(request, id):
    try:
        m = Venta.objects.get(id = id) #ver BD
    except Venta.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VentaSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Categoria(request, id):
    try:
        m = Categoria.objects.get(id = id) #ver BD
    except Categoria.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_TipoProd(request, id):
    try:
        m = TipoProd.objects.get(id = id) #ver BD
    except TipoProd.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TipoProdSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TipoProdSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Marca(request, id):
    try:
        m = Marca.objects.get(id = id) #ver BD
    except Marca.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MarcaSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Modelo(request, id):
    try:
        m = Modelo.objects.get(id = id) #ver BD
    except Modelo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ModeloSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ModeloSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Producto(request, id):
    try:
        m = Producto.objects.get(id = id) #ver BD
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Detalle(request, id):
    try:
        m = Detalle.objects.get(id = id) #ver BD
    except Detalle.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DetalleSerializer(m)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetalleSerializer(m, data = data) #ver BD
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
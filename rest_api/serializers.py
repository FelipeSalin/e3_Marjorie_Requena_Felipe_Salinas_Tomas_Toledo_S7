from rest_framework import serializers
#ejemplo
from Inicio.models import TipoUsuario, Usuario, Comuna, Region, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle 

class MarcaSerializer(serializers.ModeloSerializer):
    class Marca:
        model = Marca
        fields = ['idMarca', 'nombreMarca']
        
class ModeloSerializer(serializers.ModeloSerializer):
    class Modelo:
        model = Modelo
        fields = ['idModelo', 'nombreModelo', 'Marca']
        
class ProductoSerializer(serializers.ModeloSerializer):
    class Producto:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto','especificacionProd', 'stockProd','imagenProd', 'tipoprod', 'marca' ]
        
class DetalleSerializer(serializers.ModeloSerializer):
    class Detalle:
        model = Detalle
        fields = ['idDetalle', 'cantidad ', 'subTotal', 'venta', 'producto']
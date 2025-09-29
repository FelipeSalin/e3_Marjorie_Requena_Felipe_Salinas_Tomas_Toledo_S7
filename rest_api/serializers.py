from rest_framework import serializers
#ejemplo
from Inicio.models import TipoUsuario, Usuario, Comuna, Region, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle 

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ['idTipoUsuario', 'nombreTipo']

class UsuarioSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ['username', 'contrasennia', 'nombre', 'apellido', 'email', 'tipousuario']

class ComunaSerializer(serializers.Serializer):
    class Meta:
        model = Comuna
        fields = ['idComuna', 'nombreCom']

class RegionSerializer(serializers.Serializer):
    class Meta:
        model = Region
        fields = ['idRegion', 'nombreReg', 'comuna']

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
from Inicio.models import TipoUsuario, Usuario, Comuna, Region, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['idDireccion', 'descripcionDir', 'usuario', 'region']
    
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['idVenta', 'fechaVenta', 'usuario']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria', 'nombreCat']

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProd
        fields = ['idTiporod', 'nombreTipoProd']

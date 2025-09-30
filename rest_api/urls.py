from django.urls import path
from . import views
from rest_api.viewsLogin import login

urlpatterns = [
    path('tipousuarios/', views.lista_TipoUsuario, name = "lista_TipoUsuario"),
    path('usuarios/', views.lista_Usuario, name = "lista_Usuario"),
    path('comunas/', views.lista_Comuna, name = "lista_Comuna"),
    path('regiones/', views.lista_Region, name = "lista_Region"),
    path('direcciones/', views.lista_Direccion, name = "lista_Direccion"),
    path('ventas/', views.lista_Venta, name = "lista_Venta"),
    path('categorias/', views.lista_Categoria, name = "lista_Categoria"),
    path('tipoproductos/', views.lista_TipoProd, name = "lista_TipoProd"),
    path('marcas/', views.lista_Marca, name = "lista_Marca"),
    path('modelos/', views.lista_Modelo, name = "lista_Modelo"),
    path('productos/', views.lista_Producto, name = "lista_Producto"),
    path('detalles/', views.lista_Detalle, name = "lista_Detalle"),
    path('tipousuarios/<int:id>/', views.detalle_TipoUsuario, name = "detalle_TipoUsuario"),
    path('usuarios/<int:id>/', views.detalle_Usuario, name = "detalle_Usuario"),
    path('comunas/<int:id>/', views.detalle_Comuna, name = "detalle_Comuna"),
    path('regiones/<int:id>/', views.detalle_Region, name = "detalle_Region"),
    path('direcciones/<int:id>/', views.detalle_Direccion, name = "detalle_Direccion"),
    path('ventas/<int:id>/', views.detalle_Venta, name = "detalle_Venta"),
    path('categorias/<int:id>/', views.detalle_Categoria, name = "detalle_Categoria"),
    path('tipoproductos/<int:id>/', views.detalle_TipoProd, name = "detalle_TipoProd"),
    path('marcas/<int:id>/', views.detalle_Marca, name = "detalle_Marca"),
    path('modelos/<int:id>/', views.detalle_Modelo, name = "detalle_Modelo"),
    path('productos/<int:id>/', views.detalle_Producto, name = "detalle_Producto"),
    path('detalles/<int:id>/', views.detalle_Detalle, name = "detalle_Detalle"),
    path('login/', login, name = "login")
]

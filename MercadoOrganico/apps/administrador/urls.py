from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.index, name="index"),
    url(r'^addCatalogo/$', views.add_catalogo, name="addCatalogo"),
    url(r'^numeroCatalogo/$', views.numero_nuevo_catalogo, name="numeroCatalogo"),
    url(r'^seleccionarCatalogos/$', views.select_catalogos, name="seleccionarCatalogos"),
    url(r'^seleccionarProductos/$', views.select_productos, name="seleccionarProductos"),
    url(r'^seleccionarProducto/(?P<id>[0-9]+)/$', views.select_producto, name="seleccionarProducto"),
    url(r'^listarOfertas/(?P<productoId>.+)$', views.listarOfertas, name="listarOfertas"),
    url(r'^evaluarOfertas/$', views.evaluarOfertas, name="evaluarOfertas"),
    url(r'^ingresarCantidadAprobada/$', views.ingresarCantidadAprobada, name="ingresarCantidadAprobada")
)
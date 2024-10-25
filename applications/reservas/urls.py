# reservas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, DatosViewSet, EspaciosViewSet, MetodosPagoViewSet, HorariosDisponibleViewSet, RolesViewSet, UsuariosViewSet, ReservasViewSet, PagosViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'datos', DatosViewSet)
router.register(r'espacios', EspaciosViewSet)
router.register(r'metodos_pagos', MetodosPagoViewSet)
router.register(r'horarios_disponibles', HorariosDisponibleViewSet)
router.register(r'roles', RolesViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'reservas', ReservasViewSet)
router.register(r'pagos', PagosViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Mi API",
        default_version='v1',
        description="Descripción de la API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@miapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc
]

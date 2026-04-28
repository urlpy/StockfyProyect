from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_bien, name='registrar_bien'),
    path('buscar/', views.buscar_bien, name='buscar_bien'),
]

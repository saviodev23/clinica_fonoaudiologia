from django.urls import path
from .views.view import home
from.views.view_cliente import marcar_consulta
from.views.view_admins import marcar_consulta_cliente

urlpatterns = [
    #views
    path('', home, name="home"),
    path('marcar/consulta/', marcar_consulta, name="marcar_consulta"),
    path('marcar/consulta/', marcar_consulta_cliente, name="marcar_consulta_cliente"),
]
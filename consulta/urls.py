from django.urls import path
from django.conf import settings
# from.views.view_admins import
from .views.view import home
from.views.view_cliente import marcar_consulta
from django.conf.urls.static import static

urlpatterns = [
    #views
    path('', home, name="home"),
    path('marcar/consulta/', marcar_consulta, name="marcar_consulta"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
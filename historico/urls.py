from django.urls import path
from.views import historico
urlpatterns = [
    #views
    path('historico/', historico, name="historico"),

    ]
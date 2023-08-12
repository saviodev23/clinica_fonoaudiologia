
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts', include('accounts.urls')),
    path('', include('consulta.urls')),
    path('admin/', admin.site.urls),
    path('pagamento/', include('pagamento.urls')),
    path('historico/', include('historico.urls'))
]

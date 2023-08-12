from django.urls import path

from.views import fazer_pagamento
urlpatterns = [
    # views
    path('pagamento/', fazer_pagamento, name="pagamento"),

]
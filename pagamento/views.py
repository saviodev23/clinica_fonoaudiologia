from django.shortcuts import render

def fazer_pagamento(request):
    return render(request, 'assets/pagamento/pagamento.html')
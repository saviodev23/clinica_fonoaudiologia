from django.shortcuts import render

# Create your views here.
def marcar_consulta_cliente(request):
    return render(request, 'assets/consulta/marcar_consulta.html')
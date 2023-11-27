from django.shortcuts import render

def marcar_consulta(request):
    return render(request, 'assets/consulta/marcar_consulta.html')

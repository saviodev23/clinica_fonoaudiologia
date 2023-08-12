from django.shortcuts import render

def home(request):
    return render(request, 'assets/index.html')

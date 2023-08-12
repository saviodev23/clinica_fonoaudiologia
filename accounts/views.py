from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            group = Group.objects.get(name='Cliente')  # Obtém o grupo "Cliente"
            user.groups.add(group)  # Adiciona o usuário ao grupo "Cliente"
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.htm', {'form': form})
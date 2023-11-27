from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group, User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            user_type = form.cleaned_data.get('user_type')  # Supondo que você tenha um campo user_type no formulário
            group_name = 'Profissional' if user_type == 'profissional' else 'Paciente'
            group = Group.objects.get(name=group_name)  # Obtém o grupo correspondente
            user.groups.add(group)  # Adiciona o usuário ao grupo correspondente
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def minha_conta(request, id_user):
    dados_usuario = User.objects.get(id=id_user)

    render(request, 'registration/minha_conta.html', {'user': dados_usuario})

#adicionar depois

    # def cadastro(request):
    # if request.method == 'POST':
    #     form = CadastroForms(request.POST)
    #
    #     if form.is_valid():
    #         if form['senha'].value() != form['senha2'].value():
    #             messages.error(request, 'As senhas precisam ser iguais.')
    #             return redirect('cadastro')
    #
    #         nome = form['nome_cadastro'].value()
    #         email = form['email'].value()
    #         senha = form['senha'].value()
    #
    #         if User.objects.filter(username = nome).exists() or User.objects.filter(email = email).exists():
    #             messages.error(request, 'Email ou usuário ja cadastrado.')
    #             return redirect('cadastro')
    #
    #         usuario = User.objects.create_user(
    #             username = nome,
    #             email = email,
    #             password = senha
    #         )
    #         usuario.save()
    #         messages.success(request, f"Cadastro efetuado com sucesso!")
    #         return redirect('login')
    # else:
    #     form = CadastroForms()
    #     return render(request, 'galeria/usuarios/cadastro.html', {"form": form})
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(
        label='Tipo de Usuário',
        choices=[('paciente', 'Paciente'), ('profissional', 'Profissional')],
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'user_type']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


#Adicionar depois

# class CadastroForms(forms.Form):
#     nome_cadastro=forms.CharField(
#         label="Nome de Login",
#         required=True,
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Ex: Thiago Boiko"
#             }
#         )
#     )
#     email=forms.CharField(
#         label="Email",
#         required=True,
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Ex: thiago.boiko@boiko.com"
#             }
#         )
#     )
#     senha=forms.CharField(
#         label="Senha",
#         required=True,
#         max_length=70,
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Digite a sua senha"
#             }
#         )
#     )
#     senha2=forms.CharField(
#         label="Senha2",
#         required=True,
#         max_length=70,
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Confirme a sua senha"
#             }
#         )
#     )
#
#     def clean_nome_cadastro(self):
#         nome = self.cleaned_data.get('nome_cadastro')
#
#         if nome:
#             nome = nome.strip()
#             if ' ' in nome:
#                 raise forms.ValidationError('Espaços não são permitidos nesse campo')
#             else:
#                 return nome
from django import forms
from django.forms import ModelForm
from .models import Consulta
class FormAddConsulta(ModelForm):
    widgets = {
        'atestado': forms.FileInput(attrs={'id': 'upload', 'accept': "image/*", 'required': True})
    }
    class Meta:
        model = Consulta
        fields = "__all__"
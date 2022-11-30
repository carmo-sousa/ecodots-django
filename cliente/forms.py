from django import forms
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf_cnpj", "tipo"]

    def clean_nome(self):
        data = self.cleaned_data["nome"]

        if len(data) < 3:
            raise ValidationError("O nome deve ter 3 ou mais caracteres.")

        return data


class Form(forms.Form):
    nome = forms.CharField(max_length=100, min_length=3)

    class Meta:
        pass

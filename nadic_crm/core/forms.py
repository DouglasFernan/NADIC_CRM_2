from django import forms
from .models import Produto, Venda, Faturamento
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade_estoque', 'preco']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'quantidade']


class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = ['valor_total']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    pass

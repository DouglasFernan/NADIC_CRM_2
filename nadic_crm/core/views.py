from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Produto, Venda, models
from .forms import ProdutoForm, VendaForm
from django.db import transaction
from django.db.models import Sum, F
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import is_founder


def login_view(request):
    """
    Função de visualização para o login do usuário.
    """
    if request.method == 'POST':
        # Se a solicitação for do tipo POST, obtenha os dados do formulário de login
        username = request.POST['username']
        password = request.POST['password']
        # Autentique o usuário com as credenciais fornecidas
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Se o usuário for autenticado com sucesso, faça o login e redirecione para a página inicial
            login(request, user)
            return redirect(reverse('index'))
        else:
            # Se as credenciais forem inválidas, renderize a página de login novamente com uma mensagem de erro
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    else:
        # Se a solicitação não for do tipo POST, renderize a página de login
        return render(request, 'core/login.html')


def signup_view(request):
    """
    Função de visualização para o registro de um novo usuário.
    """
    if request.method == 'POST':
        # Se a solicitação for do tipo POST, processe os dados do formulário de registro
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            # Se os dados do formulário forem válidos, salve o novo usuário e redirecione para a página de login
            serializer.save()
            return redirect(reverse('login'))
        else:
            # Se os dados do formulário forem inválidos, renderize a página de registro novamente com uma mensagem de erro
            return render(request, 'core/signup.html', {'error': 'Failed to create user'})
    else:
        # Se a solicitação não for do tipo POST, renderize a página de registro
        return render(request, 'core/signup.html')


def index(request):
    is_founder = request.user.groups.filter(name='Fundador').exists()
    return render(request, 'core/index.html', {'is_founder': is_founder})


@login_required
def editar(request):
    """
    Função de visualização para renderizar a página de edição de produtos.
    """
    produtos = Produto.objects.all()  # Obtém todos os objetos Produto do banco de dados.
    # Renderiza o template editar.html, passando os produtos como contexto.
    return render(request, 'core/editar.html', {'produtos': produtos})


@login_required
def update(request, id):
    """
    Função de visualização para atualizar informações de um produto.
    """
    produto = get_object_or_404(
        Produto, id=id)  # Obtém o objeto Produto com o id fornecido ou retorna um erro 404 se não encontrado.
    if request.method == 'POST':
        # Preenche o formulário com os dados da requisição e do objeto Produto.
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        # Cria um formulário com os dados do objeto Produto.
        form = ProdutoForm(instance=produto)
    # Renderiza o template update.html, passando o formulário como contexto.
    return render(request, 'core/update.html', {'form': form})


@login_required
def sucesso(request):
    """
    Função de visualização para renderizar a página de sucesso.
    """
    return render(request, 'core/sucesso.html')


@login_required
def cadastrar(request):
    """
    Função de visualização para cadastrar um novo produto.
    """
    if request.method == 'POST':
        # Preenche o formulário com os dados da requisição.
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = ProdutoForm()  # Cria um formulário em branco.
    # Renderiza o template cadastro.html, passando o formulário como contexto.
    return render(request, 'core/cadastro.html', {'form': form})


@login_required
def deletar(request, id):
    """
    Função de visualização para deletar um produto.
    """
    produto = get_object_or_404(
        Produto, id=id)  # Obtém o objeto Produto com o id fornecido ou retorna um erro 404 se não encontrado.
    produto.delete()  # Exclui o objeto Produto do banco de dados.
    # Redireciona para a visualização editar.
    return HttpResponseRedirect(reverse('editar'))


@login_required
@transaction.atomic  # Se ocorrer um erro, tudo será revertido
def add_venda(request):
    """
    Função de visualização para adicionar uma nova venda.
    """
    if request.method == 'POST':
        # Preenche o formulário com os dados da requisição.
        form = VendaForm(request.POST)
        if form.is_valid():
            # Salva os dados do formulário no banco de dados, sem efetivar a transação.
            venda = form.save(commit=False)
            produto = venda.produto
            quantidade_vendida = venda.quantidade
            # Verifica se há estoque suficiente para a venda.
            if produto.quantidade_estoque >= quantidade_vendida:
                produto.quantidade_estoque -= quantidade_vendida
                produto.save()
                venda.preco_venda = produto.preco
                venda.save()
                return redirect('sucesso')
            else:
                pass
    else:
        form = VendaForm()  # Cria um formulário em branco.
    # Renderiza o template add_venda.html, passando o formulário como contexto.
    return render(request, 'core/add_venda.html', {'form': form})


@login_required
@user_passes_test(is_founder)
def faturamento(request):
    """
    Função de visualização para calcular e exibir o faturamento total.
    """
    total_faturamento = Venda.objects.aggregate(
        total_faturamento=Sum(F('preco_venda') * F('quantidade'),
                              output_field=models.DecimalField())
    )['total_faturamento']  # Calcula o faturamento total das vendas.

    vendas = Venda.objects.all()  # Obtém todas as vendas do banco de dados.

    # Renderiza o template faturamento.html, passando as vendas e o total de faturamento como contexto.
    return render(request, 'core/faturamento.html', {'vendas': vendas, 'total_faturamento': total_faturamento})

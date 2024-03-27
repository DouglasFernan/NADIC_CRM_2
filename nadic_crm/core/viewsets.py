from rest_framework import viewsets
from .models import Produto, Faturamento
from .serializers import ProdutoSerializer, FaturamentoSerializer
from rest_framework.permissions import IsAuthenticated


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


class ProdutoDetalhesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


class FaturamentoViewSet(viewsets.ModelViewSet):
    queryset = Faturamento.objects.all()
    serializer_class = FaturamentoSerializer
    permission_classes = [IsAuthenticated]

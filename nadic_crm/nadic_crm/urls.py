from core import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.viewsets import ProdutoViewSet, ProdutoDetalhesViewSet, FaturamentoViewSet
from core.views import login_view, signup_view, index, cadastrar, sucesso, editar, update, deletar, add_venda, faturamento
from django.contrib.auth import views

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/produtos/',
         ProdutoViewSet.as_view({'get': 'list', 'post': 'create'}), name='produto-list'),
    path('api/produtos/<int:pk>/', ProdutoViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='produto-detail'),
    path('api/produtos/detalhes/<int:pk>/',
         ProdutoDetalhesViewSet.as_view({'get': 'retrieve'}), name='produto-detalhes'),
    path('api/faturamento/',
         FaturamentoViewSet.as_view({'get': 'list'}), name='faturamento-list'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('sucesso/', sucesso, name='sucesso'),
    path('editar/', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('addvenda/', add_venda, name='add_venda'),
    path('faturamento/', faturamento, name='faturamento'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

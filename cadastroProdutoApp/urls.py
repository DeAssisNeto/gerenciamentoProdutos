from django.urls import path

from cadastroProdutoApp import views

urlpatterns = [
    path('produto/', views.ListCreateProduto.as_view(), name='ListCreateProduto'),
    path('produto/<int:pk>/', views.UpdateDeleteProduto.as_view(), name='UpdateDeleteProduto')
]
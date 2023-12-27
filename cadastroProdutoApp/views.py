from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cadastroProdutoApp.api.serializers import ProdutoSerializer
from cadastroProdutoApp.models import Produto


@api_view(['GET'])
def view_produto(request):
    produtos = Produto.objects.all()

    if produtos:
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


class ListCreateProduto(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class UpdateDeleteProduto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.filter(ativo=True)
    serializer_class = ProdutoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.ativo = False
        instance.save()
        if self.queryset.all():
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

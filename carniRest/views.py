from .serializers import TipoProductoSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.models import TipoProducto
from rest_framework import status

@api_view(["GET", "POST"])
def listado_categorias(request):
    if request.method == "GET":
        categorias = TipoProducto.objects.all()
        serializer = TipoProductoSerializers(categorias, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = TipoProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def categoria_especifica(request, pk):
    try:
        categorias = TipoProducto.objects.get(idTipoprod=pk)
    except TipoProducto.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = TipoProductoSerializers(categorias)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = TipoProductoSerializers(categorias, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        categorias.delete()
        return Response(status.HTTP_204_NO_CONTENT)
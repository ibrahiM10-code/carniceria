from rest_framework import serializers
from app1.models import TipoProducto

class TipoProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = "__all__"
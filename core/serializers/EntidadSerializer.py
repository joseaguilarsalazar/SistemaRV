from rest_framework import serializers
from core.models import Entidad

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'
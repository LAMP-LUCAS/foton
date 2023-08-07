# foton_system\foton_manager\serializers.py
from rest_framework import serializers
from .models import ComposicaoCusto

class ComposicaoCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComposicaoCusto
        fields = '__all__'

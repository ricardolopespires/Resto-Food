from rest_framework import serializers
from management.models import Pizzeria




class PizzeriaSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Pizzeria 
        fields = ('__all__')


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = ('__all__')
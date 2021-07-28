from rest_framework import serializers
from .models.models import Cocktails

class CocktailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2, required=True)
    price = serializers.FloatField(min_value=1, required=True)
    class Meta:
        model = Cocktails
        fields = ['id','name','price',
                  'user_id','created_at','updated_at']
        extra_kwargs = {
            'user':{'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

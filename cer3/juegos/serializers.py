from rest_framework import serializers
from juegos.models import Games
class GamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Games  
        fields = ['name', 'loaned']


       
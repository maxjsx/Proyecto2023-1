from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GamesSerializers
from .models import Games
from rest_framework import status
from django.http import Http404
    
class Games_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        games= Games.objects.all()
        serializer = GamesSerializers(games, many=True)
        
        return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        data=request.data
        games=Games.objects.filter(name=data['name']).get()
        games.loaned=data['loaned']
        games.save()
        serializer=GamesSerializers(games)
        return Response(serializer.data)
        

        
        



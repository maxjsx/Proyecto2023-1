from django.urls import path
from .views import *
app_name = 'juegos'
urlpatterns = [
    path('Games', Games_APIView.as_view()), 
    
    
    
]
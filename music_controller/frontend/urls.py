from django.urls import path
from .views import Main

app_name = 'frontend'

urlpatterns = [
    path('', Main.as_view(), name=''),
    path('info', Main.as_view()),
    path('join', Main.as_view()),
    path('create', Main.as_view()),
    path('room/<str:roomCode>', Main.as_view()),

]

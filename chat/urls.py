from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.home, name='home'),
    path('create-room/', views.create_room, name='create_room'),
    path('join-room/', views.join_room, name='join_room'),
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('leave-room/<int:room_id>/', views.leave_room, name='leave_room'),
]

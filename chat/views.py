from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room, Message, RoomMember
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

    

@login_required
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        password = request.POST.get('password')

        if Room.objects.filter(name=room_name).exists():
            messages.error(request, 'Room name already exists!')
            return redirect('chat:home')
        
        with transaction.atomic():
            room = Room.objects.create(name=room_name, password=password)
            RoomMember.objects.create(user=request.user, room=room)
        return redirect('chat:chat_room', room_id=room.id)

    return redirect('chat:home')


@login_required
def join_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        password = request.POST.get('password')
        
        try:
            room = Room.objects.get(name=room_name)
            if room.password == password:
                RoomMember.objects.get_or_create(user=request.user, room=room)
                return redirect('chat:chat_room', room_id=room.id)
            else:
                messages.error(request, 'Invalid password!')
        except Room.DoesNotExist:
            messages.error(request, 'Room does not exist!')

    return redirect('chat:home')


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    # updatee or create member status
    member, created = RoomMember.objects.get_or_create(user=request.user, room=room)
    member.is_online = True 
    member.save()
    
    # Get online members
    online_members = room.get_online_members()
    messages_list = Message.objects.filter(room=room).order_by('date')
    
    if request.method == 'POST':
        chat_message = request.POST.get('message', '')
        image = request.FILES.get('image', None)
        audio = request.FILES.get('audio', None)
        file = request.FILES.get('file', None)
        
        message = Message.objects.create(
            chats=chat_message,
            user=request.user,
            room=room,
            images=image,
            audio=audio,
            files=file
        )
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success',
                'message': 'Message sent successfully',
            })
    
    return render(request, 'room-chat.html', {'room': room, 'messages': messages_list, 'online_members': online_members,})

@login_required
def leave_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    member = get_object_or_404(RoomMember, user=request.user, room=room)
    member.is_online = False 
    member.save()
    return redirect('chat:home')
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=True)
    members = models.ManyToManyField(User, through='RoomMember', related_name='rooms')
    
    def __str__(self):
        return f"{self.name} - {self.password}"
    
    def get_online_members(self):
        return self.roommember_set.filter(is_online=True)
    

class RoomMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=True)
    last_seen = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'room')

    
class Message(models.Model):
    chats = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    files = models.FileField(upload_to='files/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}: {self.chat}"
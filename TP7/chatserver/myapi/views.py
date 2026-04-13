from rest_framework import viewsets
from .serializers import MessageSerializer, UserSerializer
from .models import Message
from django.contrib.auth.models import User

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('source')
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
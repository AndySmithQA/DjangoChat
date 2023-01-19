from django.contrib import admin
from .models import Chatrooms, ChatMessage
# Register your models here.

admin.site.register(Chatrooms)
admin.site.register(ChatMessage)
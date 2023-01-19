from django.shortcuts import render
from .models import Chatrooms
# Create your views here.

def index(request):

    chatrooms = Chatrooms.objects.all()



    return render(request, 'chatapp/index.html', {'chatrooms':chatrooms})
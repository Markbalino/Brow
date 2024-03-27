from django.shortcuts import render, HttpResponse
from .models import todoItems
# Create your views here.

def home(request):
    return render(request, "Leow.html")
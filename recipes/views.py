from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HTTP REQUEST -> HTTP RESPONSE
def home(request):
    # HTTP REQUEST
    return HttpResponse("HOME") # HTTP RESPONSE

def contato(request):
    return HttpResponse("CONTATO")

def sobre(request):
    return HttpResponse("SOBRE")
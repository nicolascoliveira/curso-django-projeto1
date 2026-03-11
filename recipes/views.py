from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HTTP REQUEST -> HTTP RESPONSE
def home(request):
    # HTTP REQUEST
    return render(request, 'recipes/home.html', context={
        'name': 'Nicolas',
        'v1': 1,
        'v2': 2,
    }) # HTTP RESPONSE

def contato(request):
    return render(request, 'temp.html')

def sobre(request):
    return HttpResponse("SOBRE")
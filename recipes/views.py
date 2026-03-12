from django.shortcuts import render
# Create your views here.

# HTTP REQUEST -> HTTP RESPONSE
def home(request):
    # HTTP REQUEST
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Nicolas',
    }) # HTTP RESPONSE

from django.shortcuts import render
from control.models import *


# Create your views here.
def index_manage_client(request):
    client = Client.objects.first() # implements the function 'firts()' don't depend on a bucle
    pet = Pet.objects.first()   
    context = {
        'client':client,
        'pet':pet
    }
    return render(request, "manage_client_index.html", context) 
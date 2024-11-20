from django.shortcuts import render
from control.models import *
from django.contrib.auth.views import LoginView


# Create your views here.
def index_manage_client(request):
    clients = Client.objects.all() # implements the function 'firts()' don't depend on a bucle
    pets = Pet.objects.all()   
    context = {
        'clients':clients,
        'pets':pets
    }
    return render(request, "manage_client_index.html", context) 


class Login(LoginView):
    template_name = 'login.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
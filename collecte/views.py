from django.shortcuts import render,redirect
from .models import Centre_Collecte,Donneur,Receveur
from django.contrib.auth import authenticate,login as auth_log
from .forms import loginForm

def index(request):
    centres=Centre_Collecte.objects.all()
    user=request.user
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')  # Redirige vers la page d'accueil si l'utilisateur n'est pas connecté
      
    
    return render(request,'index.html',locals())



    


def centreCollecte(request):
    centres=Centre_Collecte.objects.all()
    user=request.user
    return render(request,'centreCollecte.html', locals())

def donneur(request):
    donneurs=Donneur.objects.all()
    user=request.user
    return render(request, 'Donneur.html', locals())
    
def login(request):
    connection_form = loginForm()
    erreur = ""

    if request.method == "POST":
        connection_form = loginForm(request.POST)
        if connection_form.is_valid():
            username = connection_form.cleaned_data['username']
            password = connection_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_log(request, user)
                return redirect("/")
            else:
                erreur = "Nous n'avons pas reconnu votre compte."

    return render(request, 'login.html', {'connection_form': connection_form, 'erreur': erreur})

def receveur(request):
    receveurs= Receveur.objects.all()
    user=request.user
    return render(request,'receveur.html',locals())



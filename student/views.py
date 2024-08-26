from django.shortcuts import render


# Create your views here.

def index(request):
    
    context={
        'nom': "Mon nom pour l'application ",
        'prenom': "Mon prenom ",
    }
    return render(request, "student/index.html")

def edit(request):
    return render(request, "student/edit.html")

def add(request):
    return render(request, "student/add.html")
    


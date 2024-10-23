from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html',context={
        'name': 'Eduardo Ribeiro'
    })

def contato(request):
    return HttpResponse("CONTATO")

def sobre(request):
    return HttpResponse("SOBRE")

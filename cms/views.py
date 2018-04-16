# Cristina del Río 
from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse

# Create your views here.
def inicio_pag(request):
    resp = "<u><h4>La lista de las paginas es:</h4></u>"
    list_pags = Pages.objects.all()
    for pag in list_pags:
        resp += "<li><a href=" + str(pag.id) + ">" +  pag.name +  "</a></li>"
    return HttpResponse(resp)
def pag(request, id):
    pag = Pages.objects.get(id=id)
    resp = pag.name + pag.page
    return HttpResponse(resp)

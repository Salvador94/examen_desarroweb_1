# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Libro

# Create your views here.

def home(request):
    print request
    Titulo="libros"
    return render(request, 'home.html', {'TitleV': Titulo})

def lista_libros(request):
    result_set = Libro.objects.all()
    context = {
    "result": result_set
    }
    return render(request, "lista_libros.html", context)

def detalle_libro(request, id=1):
    result_set = Libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "detalle_libro.html", context)

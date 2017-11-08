# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Libro
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .forms import LibroModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

def home(request):
    print request
    Titulo = "libros"
    return render(request, 'home.html', {'TitleV': Titulo})

class LibroDeleteView(LoginRequiredMixin, DeleteView):
      model = Libro
      template_name = "Delete_confirm.html"
      success_url = reverse_lazy("lista")

class LibroUpdateView(UpdateView):
      queryset = Libro.objects.all()
      form_class = LibroModelForm
      template_name = "update_view.html"
      success_url = "Libro/lista"

class LibroCreateView(CreateView):
      form_class = LibroModelForm
      template_name = "form.html"
      success_url = "/lista"

class LibroDetailView(DetailView):
    template_name = "libros/detalle_libro.html"
    queryset = Libro.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return libro.objects.get(id=id)

    def get_context_data(self, *args, **kwargs):
        context = super(LibroDetailView, self).get_context_data(*args, **kwargs)
        print context
        return context

class LibroListView(ListView):
      template_name = "lista_libros.html"

      def get_queryset(self, *args, **kwargs):
         qs = Libro.objects.all()
         print self.request.GET
         query = self.request.GET.get("q", None)
         if query is not None:
             qs = qs.filter(
             Q(Nombre__icontains = query)|
             Q(user__username__icontains = query)
             )
             return qs
      def get_context_data(self, *args, **kwargs):
          context = super(LibroListView, self).get_context_data(*args, **kwargs)
          print context
          context['create_form'] = LibroModelForm()
          context['create_url'] = reverse_lazy("Libro_create")
          return context

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

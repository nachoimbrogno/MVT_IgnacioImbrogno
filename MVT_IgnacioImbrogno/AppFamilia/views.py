from django.http import HttpResponse
from django.shortcuts import render
from .models import Individuo

# Create your views here.

def individuo(request):

    individuo = Individuo(nombre = "Maria", apellido = "Romero",parentesco="Hermana", fechaNacimiento= "1983-05-22",telContacto= 42529831)
    individuo.save()
    texto = f"Familiar creado: nombre: {individuo.nombre} apellido: {individuo.apellido} parentesco: {individuo.parentesco} fecha de nacimiento: {individuo.fechaNacimiento} telefono de contacto: {individuo.telContacto}"
    return HttpResponse(texto)
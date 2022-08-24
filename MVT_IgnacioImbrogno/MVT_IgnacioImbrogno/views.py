from django.http import HttpResponse
from django.template import Context, Template

#Averiguo si el año de nacimiento de una persona fue bisiesto o no:
def bisiesto(request,anio):
    anio = int(anio)
    mihtml=open("D:/nacho/Desktop/MVT_IgnacioImbrogno/MVT_IgnacioImbrogno/Plantillas/template1.html")
    #Armo el if aca y no en el template porque bien como usar el if en jinja, por eso creo la  variable bandera.
    if ((anio % 4 ==0) and (anio % 100 != 0)) or (anio % 400 == 0):
        diccionario={'anio':anio, 'bandera':True}
    else:
        diccionario={'anio':anio, 'bandera':False}
    plantilla=Template(mihtml.read())
    mihtml.close()
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
    
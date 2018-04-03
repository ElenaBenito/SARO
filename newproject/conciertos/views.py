from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from models import Grupo

def barra(request):
	lista = Grupo.objects.all()		# devuelve una lista con todos los objetos de la base de datos
	# print(lista)	
	# salida = lista[0].constitucion
	salida = "<ul>"
	for grupo in lista:
		salida += '<li><a href="grupo/' + str(grupo.id) + '">' + grupo.nombre + '/a>'
	salida += "</ul>"
	# salida += formulario	# Para practica intermedia 2!!!
	return HttpResponse(salida)

@csrf_exempt			# Esta lista no va a comprobar csrf, sería un grave fallo de seguridad (no en nuestro ejemplo)
def grupo(request, numero):
	# if request.method == "POST":
		# g = Gruop(nombre = request.POST['nombre'],constitucion = request.POST['constitucion'])	# Estas tres lineas salen cuando llamamos a la barra "/" con el formulario para practia intermedia 2!!!
		# g save()
	if request.method == "PUT":
		return HttpResponse(request.body)
	try:
		grupo = Grupo.objects.get(id=int(numero))
		# grupo.id, grupo.nombre, grupo.constitucion
	except Grupo.DoesNotExist:
		return HttpResponse("No existe")	
	return HttpResponse(grupo.nombre + " " + str(grupo.constitucion))

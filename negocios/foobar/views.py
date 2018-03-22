from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Todo abajo nuevo
def barra(request):
	objeto = Genero.objects.get(id=1)
	objetos = Genero.objects.all()
	for objeto in objetos:
		string += objeto.tipo + " "
	return HttpResponse("Esto es la barra"+str(objeto.precio))

def tresas(request):
	return HttpResponse("Me has pedido tres as")

def calcular(raquest,op1,operacion,op2):
	if operacion == "suma":
		return HttpResponse("Voy a sumar: "+str(int(sumando1)+int(sumando2)))
	if operacion == "resta":
		return HttpResponse("Voy a restar: "+str(int(sumando1)-int(sumando2)))

from django.shortcuts import render
import urllib.request

# Create your views here.
global cache = {	#variable  global
}

#def barra_request(request):
#	with urllib.request.urlopen('http://gsyc.es/') as f:
#		respuesta = f.read().decode('utf-8')
#return HttpResponse(respuesta)

def buscar(request, rec):	#rec es el recurso obtenido en urls.py el primer parametro de url
	if rec in cache:
		resp = HttpResponse(cache[rec])
	else:
		with urllib.request.urlopen('http://' + rec) as w:
			pag = w.read().decode('utf-8')	#usar decode depende de si necesito un string para HttpResponse o no. VER DOCUMENTACION DE READ PARA CAPTURAR EXCEPCIONES/ERRORES
			cache[rec] = pag				#poner try y except...
			resp = HttpResponse(pag)
return resp
#..completar para llamarla desde urls.py..
def hola():
return

#!/usr/bin/python3

import webapp

contents = {
	'/lunes': 'llueve',
	'/martes': 'sol'
}

formulario = """
 <form action="" method="POST">
  Tiempo:<br>
  <input type="text" name="tiempo" value="Sol"><br>
  Donde:<br>
  <input type="text" name="donde" value=""><br>
  <input type="submit" value="Enviar">
</form> 
"""

class contentApp(webapp.webApp):
	def parse(self, request):
		return (request.split()[0], request.split()[1], request)

	def process(self, parsedRequest):  #parsedRequest es la tupla (metodo,recurso) de la petición
		metodo, recurso, peticion = parsedRequest		
		if metodo == "POST":
			todo = peticion.split('\r\n\r\n',1)[1].split('=')[1]
			contents[recurso] = todo
			
		try:
			print(contents)		
			print(recurso)
			return("200 OK", contents[recurso])
		except KeyError:
			return("404 Not Found", "<html>Resource not found!<br>" + formulario + "</html>")


if __name__=="__main__":
	testWebApp = contentApp("localhost",4567)

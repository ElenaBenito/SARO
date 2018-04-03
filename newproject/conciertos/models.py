from django.db import models

# Create your models here.
									# django 1.5(OJO) cheat sheet: https://www.mercurytide.co.uk/media/resources/django-cheat-sheet.pdf
class Grupo(models.Model):
	nombre = models.CharField(max_length=128)
	constitucion = models.DateField()
	def __str__(self):
		return self.nombre

class Componentes(models.Model):
	nombre = models.CharField(max_length=32)
	instrumento = models.CharField(max_length=32)
	grupo = models.ForeignKey(Grupo)
	def __str__(self):
		return self.nombre

class Concierto(models.Model): 
	fecha = models.DateTimeField()	# mirar las opciones de models (https://docs.djangoproject.com/en/1.8/ref/models/fields/) 
	lugar = models.CharField(max_length=32)
	precio = models.DecimalField(max_digits=6,decimal_places=2)
	num_entradas = models.IntegerField()
	grupo = models.ForeignKey(Grupo)
	def __str__(self):
		return self.grupo.nombre + "," + self.lugar + "," + str(self.fecha)


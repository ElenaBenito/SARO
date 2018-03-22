from django.db import models

# Create your models here.
#nuevo debajo
class Genero(models.Model):
	tipo = models.CharField(max_length=32)
	precio = model.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.tipo

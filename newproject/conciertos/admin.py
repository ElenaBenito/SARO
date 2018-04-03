from django.contrib import admin

# Register your models here.
from .models import Grupo, Concierto, Componentes

admin.site.register(Grupo)
admin.site.register(Concierto)
admin.site.register(Componentes)


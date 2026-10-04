from django.contrib import admin
from .models import Organismo, Usuario, Estado, Victima, Animal, Caso, Denuncia, HistorialAuditoria

admin.site.register(Organismo)
admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Victima)
admin.site.register(Animal)
admin.site.register(Caso)
admin.site.register(Denuncia)
admin.site.register(HistorialAuditoria)

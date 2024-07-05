from django.contrib import admin
from apps.core.models import Persona, Proyecto, ClientProject

admin.site.register(Persona)
admin.site.register(Proyecto)
admin.site.register(ClientProject)
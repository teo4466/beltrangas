from dataclasses import field
from django.contrib import admin
from clientes.models import Clientes

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class ClientesResource(resources.ModelResource):
    fields=(
        'nombre',
        'direccion',
        'telefono'
    )
    class Meta:
        model= Clientes

@admin.register(Clientes)
class ClienteAdmin(ImportExportModelAdmin):
    resource_class = ClientesResource
    list_display = (
        'nombre',
        'direccion',
        'telefono'
    )
    
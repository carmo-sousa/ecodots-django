from django.contrib import admin
from cliente.models import Cliente, Contato


class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cpf_cnpj", "tipo"]
    list_display_links = ["id", "nome"]
    search_fields = ["cpf_cnpj"]
    list_per_page = 20


class ContatoAdmin(admin.ModelAdmin):
    list_display = ["id", "tipo", "cliente"]
    list_display_links = ["id", "tipo"]
    search_fields = ["email", "telefone"]
    list_per_page = 20


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Contato, ContatoAdmin)

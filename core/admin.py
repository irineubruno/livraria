from django.contrib import admin
from core.models import Autor, Cliente, Editora, Escreve, Genero, ItensDaVenda, Livro, Venda
# Register your models here.

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'estoque')
    exclude = ['idgenero', 'ideditora']


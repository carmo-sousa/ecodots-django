from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from cliente.models import Cliente

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def lista(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        "lista.html",
        context={"clientes": clientes, "title": "Lista de clientes"},
    )


def detalhe(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, "detalhe.html", context={"cliente": cliente})

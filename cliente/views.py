from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import models

from .forms import ClienteForm
from cliente.models import Cliente


class Index(View):
    def get(self, request):
        form = ClienteForm()
        clientes = Cliente.objects.all()
        return render(
            request, "index.html", context={"clientes": clientes, "form": form}
        )

    def post(self, request):
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Contato salvo com sucesso!")
            return redirect("index")

        messages.add_message(request, messages.WARNING, form.errors)
        return redirect(
            to="index",
        )


# Create your views here.
def index(request):
    form = ClienteForm()
    clientes = Cliente.objects.all()

    if request.method == "POST":
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect(
            to="index",
        )

    return render(request, "index.html", context={"clientes": clientes, "form": form})


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


def deletar(request, id):
    Cliente.objects.get(pk=id).delete()
    return redirect("index")


class Editar(View):
    def get(self, request, id):
        Cliente.objects.filter(nome__endswith="Paulo")
        cliente = get_object_or_404(Cliente, pk=id)
        return render(request, "editar.html", context={"cliente", cliente})

    def post(self, request):
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf_cnpj")
        tipo = request.POST.get("tipo")

        Cliente.objects.update(nome=nome, cpf_cnpj=cpf, tipo=tipo)

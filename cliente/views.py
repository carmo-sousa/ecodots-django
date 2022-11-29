from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

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

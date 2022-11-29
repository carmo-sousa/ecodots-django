from django.urls import path
from cliente import views

urlpatterns = [
    path("", view=views.Index.as_view(), name="index"),
    path("lista", views.lista),
    path("lista/<int:id>/", views.detalhe),
]

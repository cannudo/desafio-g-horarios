from django.shortcuts import render
import requests

# Create your views here.
def listarSalas(request):
    endereco = "http://localhost:8000/api/salas"
    requisicao = requests.get(endereco)

    try:
        lista = requisicao.json()
    except ValueError:
        print("O formato da resposta não é o esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "salas": dicionario
    }

    return render(request, "salas.html", contexto)

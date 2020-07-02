from django.shortcuts import render
import requests

# Create your views here.
def listarDisciplinas(request):
    endereco = "http://localhost:8000/api/disciplinas"
    requisicao = requests.get(endereco)

    try:
        lista = requisicao.json()
    except ValueError:
        print("O formato da resposta não é o esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "disciplinas": dicionario
    }

    return render(request, "disciplinas.html", contexto)

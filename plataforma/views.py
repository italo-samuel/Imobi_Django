from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovei, Cidade
from django.shortcuts import get_object_or_404

@login_required(login_url='auth/logar')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.get('tipo')
    cidades = Cidade.objects.all()
    if preco_minimo or preco_maximo or cidade or tipo: # Verificar se foi passado algum dado em filtar

        if not preco_minimo: # Se for None
            preco_minimo = 0
        if not preco_maximo: # Se for None
            preco_maximo = 9999999999999
        if not tipo: # Se for None
            tipo = ['A', 'C']

        imoveis = Imovei.objects.filter(valor__gte=preco_minimo).filter(valor__lte=preco_maximo).filter(tipo_imovel__in=tipo).filter(cidade=cidade)
    else:
        imoveis = Imovei.objects.all()
    
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

def imovel(request, id):
    imovel = get_object_or_404(Imovei, id=id)
    return HttpResponse(id)
#from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm

import datetime


def home(request):
    data = {}
    return render(request, 'contas/home.html', data)


def listagem(request):
    transacoes = Transacao.objects.all()
    return render(request, 'contas/listagem.html', {'transacoes': transacoes})


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao

    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

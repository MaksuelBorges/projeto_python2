from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Publication
from datetime import date

def home(request):
    return render(request, 'home.html')

def blogpost_page(request):
    context = {
        'posts': Publication.objects.all()[::-1],
    }
    return render(request, 'blogpost.html', context)

def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html', {
            'incorrect_login': False 
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, Pessoa=username, password=password)
        if user is not None:
            entrar(request, user)
            return HttpResponseRedirect('/userspace')
        else:
            return render(request, 'entrar.html', {
                'incorrect_login': True 
            })
    else:
        return HttpResponseBadRequest()
    
@login_required(login_url='/entrar')
def userspace(request):
    return render(request, 'userspace.html', {
        'username': request.user.username
    })


@login_required(login_url='/entrar')
def logout(request):
    logout(request)
    return HttpResponseRedirect('/entrar')

def cadastro(request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        password = request.POST.get('password')
        pessoa = Pessoa.objects.create_user(nome, email, password)
        pessoa.nome = nome
        pessoa.sobrenome = sobrenome
        pessoa.cidade = cidade
        pessoa.estado = estado
        pessoa.email = email
        pessoa.cep = cep
        pessoa.save()
        entrar(request, pessoa)
        return HttpResponseRedirect('/userspace')
    else:
        return HttpResponseBadRequest()

def consulta(request):
    pessoas = Pessoa.objects.all()
    return render (request, 'consulta.html', {
        'pessoas' : pessoas
    })
    
def publicate(request):
    if request.method == "GET":
        return render(request, 'publicate.html')
    elif request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        file = request.FILES.get("imagem")
        publication = Publication()
        publication.autor = author
        publication.data = date.today()
        publication.conteudo = content
        publication.imagem = file
        publication.save()
        return HttpResponseRedirect('/blogpost')
    else:
        return render(request, 'publicate.html')
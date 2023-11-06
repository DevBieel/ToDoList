from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import tarefa
from django.core.paginator import Paginator
# Create your views here.

@login_required
def taskList(request):
    usuario = request.user
    primeiro_nome = usuario.nome.split()[0] if usuario.nome else '' 

    tarefas = tarefa.objects.filter(id_usuario=usuario)

    search = request.GET.get('search')

    if search:
        tarefas = tarefas.filter(titulo__icontains=search)

        if not tarefas.exists():
            messages.info(request, 'Tarefa não encontrada')
            return redirect('/')

    elif search == '':
        messages.info(request, 'Digite uma tarefa para buscar')
        return redirect('/')


    
    tarefas = tarefas.order_by('criado_em')
    paginator = Paginator(tarefas, 3)

    pagina = request.GET.get('page')
    tarefas_pagina = paginator.get_page(pagina)

    return render(request, 'tasks/lista.html', {'usuario': primeiro_nome, 'tarefas': tarefas_pagina})


def registro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']

        User = get_user_model()
        novo_usuario = User.objects.create_user(username=email, email=email, password=password, nome=nome)

        return redirect('auth/login')
    
    return render(request, 'tasks/registro.html')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'tasks/login.html')
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválido(s)')
            return render(request, 'tasks/login.html')

def user_logout(request):
    logout(request)
    return redirect('/auth/login')

@login_required
def addTask(request):
    if request.method == 'GET':
        usuario = request.user
        primeiro_nome = usuario.nome.split()[0] if usuario.nome else ''
        return render(request, 'tasks/addTask.html', {'usuario': primeiro_nome})
    else:
        usuario = request.user
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        nova_tarefa = tarefa(id_usuario=usuario, titulo=titulo, descricao=descricao)
        nova_tarefa.save()
        return redirect('/')


@login_required
def taskInfo(request, id_tarefa):
    usuario = request.user
    primeiro_nome = usuario.nome.split()[0] if usuario.nome else ''
    task = get_object_or_404(tarefa, pk=id_tarefa)
    return render(request, 'tasks/taskInfo.html', {'tarefa': task, 'usuario': primeiro_nome})

@login_required
def editTask(request, id_tarefa):
    tarefa_selecionada = get_object_or_404(tarefa, pk=id_tarefa)
    usuario = request.user
    primeiro_nome = usuario.nome.split()[0] if usuario.nome else ''

    if request.method == 'POST':
        novo_titulo = request.POST.get('novoTitulo')
        nova_descricao = request.POST.get('novaDescricao')

        tarefa_selecionada.titulo = novo_titulo
        tarefa_selecionada.descricao = nova_descricao
        tarefa_selecionada.save()

        return redirect('/')
    
    return render(request, 'tasks/editTask.html', {'tarefa': tarefa_selecionada, 'usuario': primeiro_nome})

@login_required
def deleteTask(request, id_tarefa):
    tarefa_selecionada = get_object_or_404(tarefa, pk=id_tarefa)
    tarefa_selecionada.delete()
    messages.info(request, 'Tarefa deletada com sucesso')
    return redirect('/')

def about(request):
    return render(request, 'tasks/about.html', {'about_page': True})
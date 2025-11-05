from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from projetos.models import Projeto

def listar_tarefas(request):
    #1. A busca no banco de dados
    tarefas_salvas = Tarefa.objects.all()

    #2. Criamos um "dicionário de contexto" para enviar os dados ao tempate.
    #3. A chave 'minhas_tarefas' será a variável que usaremos no HTML.
    contexto = {
        'minhas_tarefas': tarefas_salvas
    }

    #3. Renderizamos o template, passando a requisição e o contexto com s dados.
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa(request, tarefa_id):
    #busca uma  tarefa pelo id
    #se não encontrar retorna erro 404
    tarefa = get_object_or_404 (Tarefa, pk=tarefa_id)
    return render (request, 'tarefas/detalhe.html', {'tarefa': tarefa})

def adicionar_tarefa(request):
    projetos = Projeto.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        projeto_selecionado = Projeto.objects.get(pk = projeto_id)
        Tarefa.objects.create(titulo=titulo, descricao=descricao, projeto=projeto_selecionado)
        return redirect ('listar_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {'projetos':projetos})

# def alterar_tarefa(request, tarefa_id):
#     tarefa=get_object_or_404(Tarefa, pk=tarefa_id)
#     if request.method == "POST":
#         tarefa.titulo = request.POST.get('titulo')
#         tarefa.descricao = request.POST.get('descricao')
#         tarefa.save()#salva as operacoes
#         return redirect ('listar_tarefas')
#     return render(request, 'tarefas/form_tarefa.html',{'tarefa' : tarefa})

def alterar_tarefa(request, tarefa_id):
    projetos = Projeto.objects.all()
    # 1. Busca a tarefa específica que será editada ou retorna um erro 404 se não existir.
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    

    if request.method == 'POST':
        # 3. Pega os dados enviados pelo formulário.
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        projeto_id = request.POST.get('projeto') # Pega o ID do projeto selecionado no <select>.
        concluida = request.POST.get('concluida') == 'on' # Checkbox retorna 'on' se marcado.
        projeto_selecionado = get_object_or_404(Projeto ,pk = projeto_id)



        # 5. Atualiza os campos do objeto 'tarefa' que já foi carregado do banco.
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        tarefa.projeto = projeto_selecionado
        
        # 6. Salva as alterações no banco de dados.
        tarefa.save()
        
        # 7. Redireciona o usuário para a lista de tarefas após a alteração.
        return redirect('listar_tarefas')

    # 8. Se o método for GET (primeiro acesso à página de edição):
    #    Renderiza o formulário, passando a tarefa para preencher os campos
    #    e a lista de projetos para montar o seletor.
    context = {
        'tarefa': tarefa,
        'projetos':projetos,
    }
    return render(request, 'tarefas/form_tarefa.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk = tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')
    return render (request,'tarefas/confirmar_exclusao.html',{'tarefa':tarefa})

 
#métodos http
# POST: Envia dados para o servidor 
# GET: Busca dados no servidor
# PUT: Atualiza recursos existentes
# DELETE:Remove recursos seleconados 
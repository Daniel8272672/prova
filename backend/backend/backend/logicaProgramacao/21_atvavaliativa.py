import json

produtos = []
categorias = []
id_produto = 1
id_categoria = 1


def carregar_categorias():
    global categorias
    try:
        with open('categorias.json','r') as arquivo:
            categorias = json.load(arquivo)
    except:
        categorias = []


def carregar_produtos():
    global produtos
    try:
        with open('produtos.json','r') as arquivo:
            produtos = json.load(arquivo)
    except:
        produtos = []


def salvar_arquivo():
    with open('categorias.json','w') as arquivo_categoria:
        json.dump(categorias, arquivo_categoria, indent=4)
    with open('produtos.json','w') as arquivo_produto:
        json.dump(produtos, arquivo_produto, indent=4)


def cadastrar_categoria():
    global id_categoria
    carregar_categorias()
    nome = input("Digite o nome da categoria: ")
    nova = {"id_categoria": id_categoria, "nome_categoria": nome}
    categorias.append(nova)
    salvar_arquivo()
    print("Categoria cadastrada com sucesso!")
    id_categoria += 1  

def listar_categorias():
    carregar_categorias()
    if not categorias:
        print("Nenhuma categoria cadastrada.")
    else:
        for categoria in categorias:
            print("ID:", categoria['id_categoria'], "- Nome:", categoria['nome_categoria'])


def cadastrar_produto():
    global id_produto
    carregar_produtos()
    carregar_categorias()
    if not categorias:
        print("Cadastre uma categoria primeiro!")
        return
    
    listar_categorias()
    id_categoria = int(input("Digite o ID da categoria para o produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    novo = {
        "id_produto": id_produto,
        "nome_produto": nome,
        "preco": preco,
        "id_categoria_associada": id_categoria
    }
    produtos.append(novo)
    salvar_arquivo()
    print("Produto cadastrado com sucesso!")
    id_produto += 1  


def listar_produtos():
    carregar_produtos()
    carregar_categorias()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        nome_categoria = "Categoria não encontrada"
        for categoria in categorias:
            if categoria['id_categoria'] == produto['id_categoria_associada']:
                nome_categoria = categoria['nome_categoria']
                break
        print("ID:", produto['id_produto'], 
              "| Nome:", produto['nome_produto'], 
              "| Preço: R$", produto['preco'], 
              "| Categoria:", nome_categoria)


def exibir_menu():
    while True:
        print("\n--- Sistema da Loja danieletronicos ---")
        print("1. Cadastrar Categoria")
        print("2. Listar Categorias")
        print("3. Cadastrar Produto")
        print("4. Listar Produtos")
        print("5. Sair")
        opa = input("Escolha: ")
        if opa == "1":
            cadastrar_categoria()
        elif opa == "2":
            listar_categorias()
        elif opa == "3":
            cadastrar_produto()
        elif opa == "4":
            listar_produtos()
        elif opa == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

exibir_menu()

import json
produto = []
categoria = []
id_produto = 1
id_categoria = 1

def cadastrar_categoria():
    try:
        with open('categorias.json','r') as arquivo:
            categoria = json.load(arquivo)
            print ("arquivo carregado!")
    except FileNotFoundError:
        print("Arquivo categorias.json arquivo nao encontrado")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de categoria. O arquivo pode estar corrompido. Iniciando um novo arquivo.")
    
def salvar_arquivo():











def exibir_menu():
    print("---loja pede hoje faz omtem---:")
    print("1.cadastrar categoria:")
    print("2.cadastre o produto")
    print("3.gategoria associada")
    print("4.sair")


id_categoria+=1
id_produto+=1
# contexto: a biblioteca precisa de um sistema para catalogar os livro da escola. crie um sistema que salve e liste 
# os livros que devem ser salvos no arquivo biblioteca.json
# atributos necessarios 
# -titulo
# -autor
# -editora
# -ano_publicacao
# -genero
# -numero_paginas
# -idiomas
import json


def salvar_livro(livro):
    try:
        with open('biblioteca.json', 'r', encoding='utf-8') as file:
            livros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        livros = []
    
    livros.append(livro)
    
    with open('biblioteca.json', 'w', encoding='utf-8') as file:
        json.dump(livros, file, indent=2, ensure_ascii=False)
    
    print(f"Livro '{livro['titulo']}' salvo com sucesso!")

def listar_livros():
    try:
        with open('biblioteca.json', 'r', encoding='utf-8') as file:
            livros = json.load(file)
            
            if not livros:
                print("A biblioteca está vazia.")
                return
            
            print("\n--- Lista de Livros ---")
            for livro in livros:
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                print(f"Ano de Publicação: {livro['ano_publicacao']}")
                print(f"Gênero: {livro['genero']}")
                print(f"Páginas: {livro['numero_paginas']}")
                print(f"Idioma: {livro['idioma']}")
                print("-" * 20)
                
    except (FileNotFoundError, json.JSONDecodeError):
        print("A biblioteca ainda não tem livros cadastrados.")

# Menu principal
def main():
    while True:
        print("\n--- Sistema de Gerenciamento da Biblioteca ---")
        print("1. Salvar novo livro")
        print("2. Listar todos os livros")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            print("\nPreencha os dados do novo livro:")
            titulo = input("Título: ")
            autor = input("Autor: ")
            editora = input("Editora: ")
            ano_publicacao = int(input("Ano de Publicação: "))
            genero = input("Gênero: ")
            numero_paginas = int(input("Número de Páginas: "))
            idioma = input("Idioma: ")
            
            novo_livro = {
                "titulo": titulo,
                "autor": autor,
                "editora": editora,
                "ano_publicacao": ano_publicacao,
                "genero": genero,
                "numero_paginas": numero_paginas,
                "idioma": idioma
            }
            salvar_livro(novo_livro)
            
        elif escolha == '2':
            listar_livros()
            
        elif escolha == '3':
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

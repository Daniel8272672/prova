import json

def cadastrar_usuario():
    """
    Função para coletar os dados de um novo usuário.
    Retorna um dicionário com os dados do usuário.
    """
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    cidade = input("Digite a cidade: ")
    
    # Validação da idade com try/except
    while True:
        try:
            idade = int(input("Digite a idade: "))
            break
        except ValueError:
            print("Idade inválida. Por favor, digite um número.")
    
    sexo = input("Digite o sexo: ")
    
    return {
        "nome": nome,
        "telefone": telefone,
        "cidade": cidade,
        "idade": idade,
        "sexo": sexo
    }

def main():
    """
    Função principal do programa.
    Gerencia a leitura, cadastro e salvamento dos dados.
    """
    nome_arquivo = "usuarios.json"
    usuarios = []

    # Carregar dados do arquivo, se ele existir
    try:
        with open(nome_arquivo, "r") as arquivo:
            usuarios = json.load(arquivo)
        print(f"Dados existentes carregados com sucesso do arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando um novo cadastro.")
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo '{nome_arquivo}'. O arquivo pode estar corrompido. Iniciando um novo cadastro.")
    
    # Laço principal para o cadastro
    while True:
        novo_usuario = cadastrar_usuario()
        usuarios.append(novo_usuario)
        
        continuar = input("\nDeseja cadastrar outro usuário? (s/n): ").lower()
        if continuar != 's':
            break

    #Salvar a lista atualizada no arquivo
    try:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        print(f"\nTodos os usuários foram salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"\nOcorreu um erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()

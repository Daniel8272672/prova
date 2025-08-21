#O try/except em Python é um mecanismo para tratamento de exceções, permitindo que o código continue a ser executado mesmo quando ocorrem erros. O bloco try contém o código que pode gerar uma exceção. Se uma exceção ocorrer nesse bloco, o controle é transferido para o bloco except correspondente, onde um tratamento pode ser aplicado. Se nenhuma exceção ocorrer no bloco try, o bloco except é ignorado. 
#exemplo1
#try:
    #x = int(input("Digite um número: "))
    #resultado = 10 / x
    #print(f"O resultado da divisão é: {resultado}")
#except ValueError:
    #print("Erro: Digite um número inteiro válido.")
#except ZeroDivisionError:
    #print("Erro: Não é possível dividir por zero.")
#except Exception as e:
    #print(f"Ocorreu um erro inesperado: {e}")
#else:
    #print("Operação realizada com sucesso!")
#finally:
    #print("Programa finalizado.")
#exemplo 2
try:
    # Código que pode gerar uma exceção
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ZeroDivisionError:
    # Código executado se ocorrer uma exceção de divisão por zero
    print("Erro: Divisão por zero não é permitida.")

except ValueError:
    # Código executado se ocorrer um erro de valor (entrada inválida)
    print("Erro: Entrada inválida. Digite um número.")

except Exception as e:
    # Código executado para qualquer outro tipo de exceção
    print(f"Ocorreu um erro inesperado: {e}")

else:
    # Código executado se nenhuma exceção ocorrer no bloco try
    print("Operação concluída com sucesso!")

finally:
    # Código executado sempre, independentemente de exceções
    print("Fim do bloco try/except.")
  
 
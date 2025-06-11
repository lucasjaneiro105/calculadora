def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (**)")
    print("6. Raiz quadrada (√)")
    print("7. Sair")

    while True:
        try:
            operacao = input("\nEscolha a operação (1-7): ")
            
            if operacao == '7':
                print("Obrigado por usar a calculadora!")
                break
                
            if operacao == '6':
                num = float(input("Digite o número: "))
                if num < 0:
                    print("Não é possível calcular raiz quadrada de número negativo!")
                    continue
                resultado = num ** 0.5
                print(f"Raiz quadrada de {num} = {resultado}")
                continue
                
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == '1':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
            elif operacao == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                    continue
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            elif operacao == '5':
                resultado = num1 ** num2
                print(f"{num1} ** {num2} = {resultado}")
            else:
                print("Operação inválida!")
                
        except ValueError:
            print("Erro: Por favor, digite números válidos!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    calculadora() 

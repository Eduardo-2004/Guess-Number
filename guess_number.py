
import random

print("\nSeja muito bem vindo(a) ao Guess Number do Edu")

max_number = input("\nDigite o número máximo do desafio: ")

if max_number.isdigit():
   max_number = int(max_number)
else:
    print("Valor informado é invalido. Tente novamente!")
    quit() 

random_number = random.randint(0, max_number) 

n_choices = 0

while True: 
    answer_user = input("Adivinhe o numero: ")

    #Verificacao de numero
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else: 
        print("\nErro: Valor informado é invalido. Por favor, informe um valor numérico!\n ")        
        continue
   
    #tentativas
    n_choices = n_choices + 1 

    #Dicas/Resposta
    if answer_user == random_number:
        print("\n|Acertouuuuuuu|")
        break
    elif answer_user > random_number:
        print("\nChutou Alto, O número randomico é 'menor' que isso...")
    else:
        print("\nChutou baixo, o número randomico é 'maior' que isso...")

print("[Tentativas: " + str(n_choices) + "]")
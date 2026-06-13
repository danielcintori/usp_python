# num_inteiro = 7
# print(type(num_inteiro))
# print(num_inteiro)
# tranformando_em_numero_com_fracao = float(num_inteiro)
# print(type(tranformando_em_numero_com_fracao))
# print(tranformando_em_numero_com_fracao)
# voltando_pra_inteiro = int(tranformando_em_numero_com_fracao)
# print(type(voltando_pra_inteiro))
# print(voltando_pra_inteiro)
# mudar_para_texto = str(voltando_pra_inteiro)
# print(type(mudar_para_texto))
# print(mudar_para_texto)

# print('que bagunça boa kkk')

# nome_usuario = 'Cleber'
# print(f'Bom dia {nome_usuario}, você acordou tarde hoje hein...')

# primeiro_numero = int(input('Digite um número para ser somado: '))
# segundo_numero = int(input('Digite um segundo número para ser somado: '))

# soma = primeiro_numero + segundo_numero

# print(f'A soma entre {primeiro_numero} e {segundo_numero} é igual a {soma}')

# if(soma >= 30):
#         print('A soma é maior ou igual a 30!')
# else:
#     print('A soma é menor que 30!')


# for i in range(10):
#     print(i)

# print(f'------ print de separação ----')
# contador = 0
# while (contador < 10 ):
#     print(contador)
#     contador = contador + 1


# import random

# resp = 0
# random_number  = random.randint(1,10)

# print('\n---Gerador de números aleatórios automáticos---')
# print(f'Aqui está o seu primeiro número aleatório: {random_number}')
# print("Posso gerar quantos números aleatórios de 1 a 10 você quiser.")

# resp = int(input('\n Se deseja gerar outro número aleatório, digite "0" '))

# while (resp == 0):
#     print(f' \n Seu novo número aleatório é: {random.randint(1,10)}')
#     resp = int(input('\n Se deseja gerar outro número aleatório, digite "0" '))
    
#     if(type(resp) != Number):
#         print(f'Entrada inválida')

# print('\n\n Obrigado e até mais!')


print('--- Simple Calculator ---')


first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

print('\nNow choose the operation by typing the correct number:')
print('Type 1 to sum')
print('Type 2 to subtract')
print('Type 3 to multiply')
print('Type 4 to divide')

choose = int(input('Select operation here: '))


result_sum = first_number + second_number
result_subtract = first_number - second_number
result_multiply = first_number * second_number
result_divide = first_number / second_number


if choose == 1:
    print(f'The sum of {first_number} and {second_number} is equal to {result_sum}')
elif choose == 2:
    print(f'The subtraction of {first_number} and {second_number} is equal to {result_subtract}')
elif choose == 3:
    print(f'The multiplication of {first_number} and {second_number} is equal to {result_multiply}')
elif choose == 4:
    print(f'The division of {first_number} and {second_number} is equal to {result_divide}')
else:
    print('Invalid option!')

print('\nThanks for using! If you need help with math, you are welcome to come back.')




import random

print("\n--- Gerador de números aleatórios automáticos ---")
print(f"Aqui está o seu primeiro número aleatório: {random.randint(1, 10)}")
print("Posso gerar quantos números aleatórios de 1 a 10 você quiser.")

while True:
    try:
        resp = int(input('\nSe deseja gerar outro número aleatório, digite "0": '))

        if resp == 0:
            print(f"\nSeu novo número aleatório é: {random.randint(1, 10)}")
        else:
            break

    except ValueError:
        print("Entrada inválida! Digite apenas números.")

print("\nObrigado e até mais!")



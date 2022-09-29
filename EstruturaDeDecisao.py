#Estrutura de Decisão

#URL: https://wiki.python.org.br/EstruturaDeDecisao

# 1 - Faça um Programa que peça dois números e imprima o maior deles.

from audioop import reverse


n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

if(n1 > n2):
    print("O maior número é: ",n1,".")
elif(n2 > n1):
    print("O maior número é: ",n2,".")   
elif(n1 == n2):
    print("O número ",n1,"é igual ao ",n2,".")    

# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Informe o valor: "))

if(valor < 0):
    print("O valor é negativo")
elif(valor > 0):
    print("O valor é positivo")
elif(valor == 0):
    print("O valor é zero.")
    
# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite F ou M: ")

if(letra == "F" or letra == "f"):
    print("Você digitou a letra ",letra," - Feminino.")
elif(letra == "M" or letra == "m"):
    print("Você digitou a letra ",letra," - Masculino.")
else:
    print("Você digitou um Sexo Inválido.")


# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def vogal(v):
    if(v in "aeiou"):
        print("Você digitou uma vogal")
    elif(v in "0123456789"):
        print("Você digitou um número")  
    else:
        print("Você digitou uma consoante")

v = input("Digite uma letra: ")
vogal(v)

# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
'''
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
média = (nota1+nota2)/2

if(média >= 7.0):
    print("Sua média é ",média," , você foi aprovado.")
elif(média <7.0):
    print("Sua média é ",média," , você foi reprovado.")
elif(média == 10.0):
    print("Sua média é ",média," , você foi aprovado com distinção, parabéns!")

# 6 - Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if(numero1 > numero2 and numero1 > numero3):
    print("O maior valor digitado foi: ",numero1,".")
elif(numero2 > numero1 and numero2 > numero3):
    print("O maior valor digitado foi: ",numero2,".")
elif(numero3 > numero1 and numero3 > 2):
    print("O maior valor digitado foi: ",numero3,".")

# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.



# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

if(produto1 < produto2 and produto1 < produto3):
    print("O produto de menor valor custa R$: ",produto1,".")
elif(produto2 < produto1 and produto2 < produto3):
    print("O produto de menor valor custa R$: ",produto2,".")
elif(produto3 < produto1 and produto3 < produto2):
    print("O produto de menor valor custa R$: ",produto3,".")

# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

lista = [numero1,numero2,numero3]
lista.sort(reverse = True)
print(lista)


# 10 - Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite M para Matutino, V para Vespertyino ou N para Noturno: ")

if(turno == "V" or turno == "v"):
    print("Boa tarde!")
elif(turno == "M" or turno == "m"):
    print("Bom dia!")
elif(turno == "N" or turno == "n"):
    print("Boa noite!")
else:
    print("Você digitou um turno inválido.")

# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores, 
# e lhe contraram para desenvolver o programa que calculará os reajustes.
'''
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
Faixa 1 - salários até R$ 280,00 (incluindo) : aumento de 20%
Faixa 2 - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
Faixa 3 - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
Faixa 4 - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input("Digite aqui o valor do seu salário: "))
def faixa1():
    reajuste = salario*0.2
    novoSalario = salario+reajuste
    print("O salário atual é de R$ ",salario," reais.\nO percentual de aumento aplicado foi de 20%.\nO valor do aumento foi de ",reajuste," reais.\nO novo salário após o aumento é de ",novoSalario," reais.")

def faixa2():
    reajuste = salario*0.15
    novoSalario = salario+reajuste
    print("O salário atual é de R$ ",salario," reais.\nO percentual de aumento aplicado foi de 15%.\nO valor do aumento foi de ",reajuste," reais.\nO novo salário após o aumento é de ",novoSalario," reais.")

def faixa3():
    reajuste = salario*0.1
    novoSalario = salario+reajuste
    print("O salário atual é de R$ ",salario," reais.\nO percentual de aumento aplicado foi de 10%.\nO valor do aumento foi de ",reajuste," reais.\nO novo salário após o aumento é de ",novoSalario," reais.")

def faixa4():
    reajuste = salario*0.05
    novoSalario = salario+reajuste
    print("O salário atual é de R$ ",salario," reais.\nO percentual de aumento aplicado foi de 5%.\nO valor do aumento foi de ",reajuste," reais.\nO novo salário após o aumento é de ",novoSalario," reais.")

if(salario <= 280.0):
    faixa1()
if(salario > 280.0 and salario <= 700.0):
    faixa2()
if(salario >700.0 and salario <=1500.0):
    faixa3()
if(salario >1500.0):
    faixa4()

# 12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
'''
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''
# 13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

# 14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
'''
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
  e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

'''
# 15 - Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
# 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

'''
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
# 17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# 19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
'''
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
# 20 - Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:
'''
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
média = (nota1+nota2)/2

if(média >= 7.0):
    print("Sua média é ",média," , você foi aprovado.")
elif(média <7.0):
    print("Sua média é ",média," , você foi reprovado.")
elif(média == 10.0):
    print("Sua média é ",média," , você foi aprovado com distinção, parabéns!")


# 21 - Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
'''
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
uma nota de 5 e quatro notas de 1.
'''
# 22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

# 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

# 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
'''
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
# 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
'''
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
# 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
'''
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
# 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
'''
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
# 28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
'''
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''




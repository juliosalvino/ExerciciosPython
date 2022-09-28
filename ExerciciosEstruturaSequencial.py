#Estrutura Sequencial

#URL: https://wiki.python.org.br/EstruturaSequencial

#1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("Alô Mundo!")

#2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

número = input("Informe um número: ")
print("O número informado foi: ",número)

#3 - Faça um Programa que peça dois números e imprima a soma.

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
soma = n1+n2
print("A soma de ", n1, " e ", n2, " é ",soma)


#4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

media1 = float(input("Informe a primeira média: "))
media2 = float(input("Informe a segunda média: "))
media3 = float(input("Informe a terceira média: "))
media4 = float(input("Informe a quarta média: "))

mediafinal = (media1+media2+media3+media4)/4

print("A média final é :",mediafinal)

#5 - Faça um Programa que converta metros para centímetros.

metragem = float(input("Informe a metragem: "))

centimetros = metragem/100
print(metragem," metros é igual á ",centimetros,"centimetros")

#6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Informe o tamanho do raio: "))

area = 3,14 * raio**2
print("A área do círculo é: ",area)

#7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lateral = float(input("Informe o valor da lateral do quadrado: "))

areadobrada = 2* (lateral*lateral)

print("O valor dobrado da área do quadrado é: ",areadobrada)

#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

horas = float(input("Informe o total de horas trabalhadas no mês: "))
valor = float(input("Informe o valor da hora trabalhada: "))

salario = horas * valor

print("O seu salário mensal é: ",salario)

#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

Fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
celsius = 5* ((Fahrenheit-32)/9)

print("A temperatura em Celsius é de: ",celsius," graus.")

#10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius1 = float(input("Informe a temperatura em Celsius: "))
Fahrenheit1 = (celsius1*1.8) +32
print("A temperatura em Fahrenheit é de: ",Fahrenheit1," graus.")

#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

n11 = int(input("Informe o primeiro número: "))
n22 = int(input("Informe o segundo número: "))
n33 = float(input("Informe o terceiro número: "))

#a - o produto do dobro do primeiro com metade do segundo .

soma = (n11*2)+(n22/2)
print(soma)

#b - a soma do triplo do primeiro com o terceiro.

soma2 = (n11*3)+n33
print(soma2)

#c - o terceiro elevado ao cubo.

soma3 = n33**3
print(soma3)

#12 - Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Informe sua altura: "))

pesoIdeal = (72.7*altura)-58
print("O seu peso ideal é: ",pesoIdeal)

#13 - Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura1 = float(input("Informe sua altura: "))
genero = input("Informe seu genero: ")

if(genero == "masculino"):
    pesoIdeal1 = (72.7*altura1) - 58
    print("O seu peso ideal é: ",pesoIdeal1)
elif(genero == "feminino"):
    pesoIdeal1 = (62.1*altura1) - 44.7
    print("O seu peso ideal é: ",pesoIdeal1)
else:
    print("Genero incorreto, digite masculino ou feminino.")  


#14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos),
#  deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.



pesoPeixe = int(input("Informe o peso do peixe: "))

if (pesoPeixe > 50):
    excesso = pesoPeixe - 50
    multa = excesso*4
    print("O peso do seu peixe é de ",pesoPeixe,", ele possui ",excesso," quilos de excesso, e este excesso gerou uma multa de ", multa," reais.")
else:
    print("O peso do peixe é de ", pesoPeixe," , e de acordo com o regulamento do Estado de São Paulo, não gerou multa, pois não houve excesso.")


#15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:


horasTrabalhadas = float(input("Informe o total de horas trabalhadas no mês: "))
valorHora = float(input("Informe o valor da hora trabalhada: "))

salarioBruto = horasTrabalhadas*valorHora
IR = salarioBruto*0.11
INSS = salarioBruto*0.08
sindicato = salarioBruto*0.05
salarioLiquido = salarioBruto - IR - INSS - sindicato

print("Salário Bruto: R$ ",salarioBruto)
print("IR: R$ ",IR)
print("INSS: R$ ",INSS)
print("Sindicato: R$ ",sindicato)
print("Salário Líquido: R$ ",salarioLiquido)


#16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math as mt
metrosQuadrados = float(input("Informe a metragem do local a ser pintado: "))

litros = metrosQuadrados/3
litrosInteiros = mt.ceil(litros)
latas = litrosInteiros/18
latasInteiras = mt.ceil(latas)

valorPago = latasInteiras*80

print("Para pintar ",metrosQuadrados," metros, você irá precisar de ",latasInteiras," latas, que irá custar ",valorPago," reais.")


#17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.



#18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input("informe o tamanho do arquivo em MB: "))
velocidade = int(input("informe a velocidade de download da sua rede: "))

segundos = tamanhoArquivo/velocidade
if(segundos<60):
    print("O download ocorrerá em ",segundos," segundos.")
elif(segundos == 60):
    print("O download ocorrerá em 1 minuto.") 
elif(segundos>60):
    tempo = segundos//60
    segundosRestantes = int(segundos%60)
    print("O download ocorrerá em ",tempo," minutos e ",segundosRestantes," segundos.")      

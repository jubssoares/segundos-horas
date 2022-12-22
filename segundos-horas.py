# Escreva um programa Python que recebe um valor qualquer t, em segundos (fornecido pelo usuário), e o imprime no formato horas:minutos:segundos.

#Interação com o usuário
print("Conversor de segundos em hh:MM:ss\n")

valorT = eval(input("Insira um valor em segundos: "))

#Definição das variáveis e conversão
horas = valorT / 3600
resto = valorT % 3600
minutos = resto / 60
segundos = resto % 60

#Informando ao usuário
print(valorT, " segundos = ", round(horas), "h:", round(minutos), "min:", round(segundos), "s")
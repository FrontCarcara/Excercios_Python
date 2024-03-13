numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    n = int(input('Digite um numero: '))
    if 0<= n<= 20:
        break
    print('Tente novamente!', end='')
print(f' Você digitou: {numeros[n]}')









    #while n not in "0" and "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" and "10" and "11" and "12" and "13" and "14" and "15" and "16" and "17" and "18" and "19" and "20":
        #n = int(input('Digite um numero: '))

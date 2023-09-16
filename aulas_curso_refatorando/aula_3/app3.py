import math

num1 = 200
num2 = 10.75

a = float(num1)
b = int(num2)

a = int("200")
b = int(float("10.75"))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 // num2) #Tira as casas decimais
# print(num1 % num2)  #Resto da divisão
# print(num1 * num2)
# print(num1 ** num2) #Exponenciação

# print(abs(-15 * -1000))      #Número absoluto, ou seja, tira o sinal de -
# print(pow(15,100))           #15 elevado a 1000 = 15 * 15 * ... * 15 * 15 * 15
# print(max(5,1000,15,-55,75)) #Mostra o maior número em uma lista de números 
# print(min(5,1000,15,-55,75)) #Mostra o menor número em uma lista de números 
# print(round(8.8))            #Arendonda para cima ou para baixo de jeito "inteligente" 
# print(round(8.3))            

#Chama a função math
print(math.floor(8.999)) #aredonda para baixo independente do que há depois da vírgula
print(math.ceil(8.001))  #aredonda para cima independente do que há depois da vírgula
print(math.sqrt(25))     #mostra o valor de raíz quadrada de tal número

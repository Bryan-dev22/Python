minha_string1 = "Qualquer Texto"
minha_string2 = "qualquer texto"
minha_string3 = " qualquer texto "

# print(f"Concatenar {minha_string} em string")

# print(minha_string1.upper())      #todas da string em maiúscula
# print(minha_string1.lower())      #todas da string em minúscula
# print(minha_string2.capitalize()) #primeira da string em maiúscula
# print(minha_string2.isupper())    #verifica se a string é maiúscula
# print(minha_string2.islower())    #verifica se a string é minúscula
# print(minha_string3.strip())      #tira os espaços de antes e depois da string

# print(minha_string2.replace("qualquer","meu")) #substitui a palavra qualquer por meu
# print(minha_string2.replace("e","E",1))        #substitui a letra e por E uma vez

# print(len(minha_string2)) #verifica o tamanho da string

#                                  qualquer texto
#                                  01234567891111
#                                       01234  
# print(minha_string2[4]) #          q
# print(minha_string2[0:8]) #        qualquer
# print(minha_string2[-14:-6]) #     qualquer
# print(minha_string.index("u"))#     1
# print(minha_string.index("quer"))#     4

# x = "texto" in minha_string2
# print(x)

# y = "Oi" in minha_string2
# print(y)

minha_string = "linha1,\nlinha2\n,\"linha3.\"" #\n para quebrar linha e \" para adicionar "
print(minha_string)

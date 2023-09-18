# def big_mac():
#     print("Sanduíche big mac")

# big_mac()

def fazer_big_mac(nome):
    print(f"Sanduíche big mac {nome}")

def fazer_batata(tamanho):
    print(f"Batata {tamanho}")

def servir_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

# fazer_big_mac(Bryan)
# fazer_batata("Grande")
# servir_refrigerante("Coca","Médio")

def combo_bigmac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    servir_refrigerante(tipo_refri,tamanho_refri)

# combo_bigmac("Bryan","Grande","Coca","Grande")

def soma(num1,num2):
    return num1 + num2

resultado = soma(15,20)

# print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num(2132341,221,-3214,2322,1)

print(resultado)
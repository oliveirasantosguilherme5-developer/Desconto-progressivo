#Sistema de desconto progressivo
#Autor: Guilherme Oliveira Santos

valor_compra = float(input(" Digite o valor da compra: R$ "))


#Porcentagem de desconto progressivo

if valor_compra < 200:
    desconto = 0.05
elif valor_compra < 300:
    desconto = 0.10
else:
    desconto = 0.15

valor_final = valor_compra - (valor_compra * desconto)

print("Você ganhou um desconto de", desconto * 100, "%.")
print("Valor final a pagar: R$", valor_final)
#1. Tipagem de variáveis

# Variáveis são recursos usados para armazenar valores em memória
# Possuímos diversos tipos de variáveis, tais como inteiros, strings, booleanos, etc.

a = 5
print(type(a))

b = 'ônibus'
print(type(b))

c = True
print(type(c))

# Em Python, as variáveis são dinâmicas, ou seja, podem mudar seu tipo ao longo do código.

d = 4
print(type(d))
d = '4'
print(type(d))

# Além disso, as variáveis possuem tipagem forte, o que significa que não podemos operar com 2 tipos de variáveis diferentes

a = 5
b = '3'
# print(a + b)    #TypeError

# O tipo string pode ser concatenado usando +
var1 = "Olá"
var2 = "Mundo"
print(var1 + ' ' + var2)


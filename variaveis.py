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

#2. Tipos de dados em Python

# Python apresenta tipos de dados padrões das linguagens de programação
# Float -> Números reais
# Int -> Números inteiros
# Strings -> Palavras
# Bool -> Booleanos (True, False)

# Assim como tipos "novos", que seriam próximos de Arrays de outras linguagens (todavia, não são iguais, e Python contém uma biblioteca para Arrays
# , chamada de Numpy), esses tipos armazenam outros tipos de dados, tratando os conteúdos armazenados de formas diferentes, são eles:

# a) Listas (lists), que armazenam dados mutáveis e possuem formas de colchetes:

v = [1, 2, 3]
type(v)

# b) Tuplas (tuples), que armazenam dados imutáveis e possuem formas de parenteses:

v = (1, 2, 3)
type(v)

# c) Dicionários (dics), que armazenam dados atribuindo uma chave para cada um e possuem formas de chaves:

v = {a:"1", b:"2", c:"3"}
type(v)

# Além delas, existem outras coleções que podem ser utilizadas, disponíveis em https://docs.python.org/3/library/collections.html
# Falaremos de coleções e operações com elas em outro momento.

#3. Entrada e saída de variáveis

# Em Python, temos duas funções importantes para trabalhar com variáveis: print e input
# A saída é feita com a função Print, que mostra qualquer tipo de dado desejado

print("Hello World!")

# A entrada é feita com a função Input, que armazena um dado do usuário para a variável atribuida

v = input("Informe o dado desejado para armazenamento: ")
print(v)

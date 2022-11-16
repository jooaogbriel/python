#comentário

"""
comentário 
"""

def minha_funcao():
    return 'Hello Word'

print(type(minha_funcao))
print(minha_funcao)

my_integer = 10
print(type(my_integer)) #int

my_string = 'minha string'

my_boolean = True

x = 5

if x > 5:
    print('x é maior 5')
elif x == 5:
    print('x é igual a 5')
else:
    print('x é menor que 5') 

x = 6
y = 10

if x == 5 and y == 10:
    print('x = 6 e y = 10')

if x == 5 or y == 10:
    print('OU')

if not x == 20:
    print('x nao é 20')
    
my_string = 'x-salada'

if 'x' in my_string:
    print('x encontrado')

if 'z' not in my_string:
    print('z nao encontrado')

my_string = 'Olá M5!'

for char in my_string:
    print(char)

for index, char in enumerate(my_string):
    print(index, char)

for number in range(10):
    print(number)

for number in range(0,10,2):
    print(number)






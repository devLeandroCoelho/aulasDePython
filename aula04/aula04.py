"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 12345 0 -10 -20 -40
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/logico - True/False 10==10
"""

print('Luiz', type('Luiz'))
print(10, type(10))
print(29.32, type(29.32))
print('L' == 'L', type('L' == 'L'))

#Convertendo Tipos

print('1',type('1'), int('1'))
print(1,type(1),'1',type(str(1)))

#exercicio

#String: Nome
print('Leandro Coelho', type('Leandro Coelho'))
# Int: Idade
print(37, type(37))
#Float: Altura
print('1.74', type('1.74'))

# É Maior de idade?
print(37 > 18, type(37>18))

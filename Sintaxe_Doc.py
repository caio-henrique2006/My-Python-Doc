'''
 Aqui guardo toda a sintaxe da linguagem de programação Python já estudada por
 mim: Caio Henrique;
'''

# Operators:
print("\nExemplo Operadores")
print(3 + 4) # Soma
print(3 - 4) # Subtração
print(3 * 4) # Multiplicação
print(3 / 4) # divisão
print(10 % 9) # divisão retorna resto
print(3 ** 4) # potenciação
print(3 // 4) # divisão retorna apenas o valor inteiro
a = 4
a += 3
'''
Assignment operator:
 +=
 -=
 *=
 /=
 %=
 //=
 **=
'''
print(a)

# Variable:
'''
    ~name~ = ~value~
'''

carteira = 200 # int value
name = "Caio Henrique" # string value
porcentagemDeGanho = 2.5 # float value
caioGanhou = True # boolean value

# if else elif:
'''
    if(~boolean~):
        ~code~
    elif(~boolean~):
        ~code~
    else:
        ~code~
'''

print("\nExemplo if, else, elif: ")
dinheiroCarteira = 200
if(dinheiroCarteira >= 200):
    print("Carteira com mais de 200 reais")
elif(dinheiroCarteira < 200):
    print("Carteira com menos de 200 reais")
else:
    print("Não sei quanto de dinheiro tem na carteira")

# For:
print("\nExemplo For: ")
'''
for ~variable~ in ~list~:
    ~code~
'''

for a in range(0,11):
    print("I'm ", a, "years old")

# Class:
print("\nExemplo de Classe: ")

class Calculator():
    
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        
    def somar(self):
        return self.firstNumber + self.secondNumber
    def subtracao(self):
        return self.firstNumber - self.secondNumber
    def multiplicacao(self):
        return self.firstNumber * self.secondNumber
    def divisao(self):
        return self.firstNumber / self.secondNumber

print(Calculator(5, 6).multiplicacao())




























































































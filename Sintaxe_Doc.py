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

# While:
print("\nExemplo While: ")

condition = 1
while(condition <= 10):
    print("condition is now ", condition)
    condition += 1

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

# Dictionaries:
print("\nExemplo de Dictionaries: ")

market = {"applePrice":20, "bananaPrice":10, "eggPrice":5}
for i in market:
    print(i, market[i])

# Formating:
print("\nExemplo de Formatting: ")

print("%s buy a %d dollars coffe and a %1.2f bread." %("Caio", 2, 3.25))
print("His name is {name}. {name} bought a car for {carPrice} dollars.".format(name="Caio",carPrice=200000))

# Functions:
print("\nExemplo Functions: ")

'''
def ~functionName~(~arguments~):
    ~code~
    return ~code~
'''

def bewareWith(scaryThing):
    bewareSentence = "beware with " + scaryThing
    return bewareSentence

print(bewareWith("Baba Yaga"))

# Lists:
print("\nExemplo Lists: ")

marketList = ["apples", "bananas", "meat", "eggs", "cheese"]
print(marketList[2])

# Tuple:
# Tuples are lists that cannot be changed:
marketList = (1,2,3)

# Open files:
print("\nExemplo open files: ")
text = open("textTest.txt", "r") # open and read file
print(text.read(1))
print(text.readline())
print(text.read())
text.close()
text = open("textTest.txt", "a") # open and append file
text.write("\nNew line for you baby")
text.close()
'''
text = open("textTest", "w") # open and delete all the content for writting
a new one
'''

# Methods and native functions:

# List methods:
'''
sample = [1,2,2,3,4,5,6,7]
sample.append(x) # Acrescenta 'x' um valor no final da lista
sample.count(x) # conta quantos 'x' tem na lista
sample.index(x) # retorna o index do primeiro elemento 'x'
sample.insert(y,x) # substituí 'y' por 'x'
sample.pop() # retorna último elemento
sample.remove(x) # remove 'x'
sample.reverse() # retorna a lista ao contrário
sample.sort() # organiza em ordem alfábetica ou númerica ascendente
'''
# String methods:
'''
stringVar.count(‘x’) – counts the number of occurrences of ‘x’ in stringVar
stringVar.find(‘x’) – returns the position of character ‘x’
stringVar.lower() – returns the stringVar in lowercase (this is temporary)
stringVar.upper() – returns the stringVar in uppercase (this is temporary)
stringVar.replace(‘a’, ‘b’) – replaces all occurrences of a with b in the string
stringVar.strip() – removes leading/trailing white space from string
'''









































































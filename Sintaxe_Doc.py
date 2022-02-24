'''
 Aqui guardo toda a sintaxe da linguagem de programação Python já estudada por
 mim: Caio Henrique;
'''

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

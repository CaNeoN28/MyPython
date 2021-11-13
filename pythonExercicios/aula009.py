frase = 'Estou aprendendo Python'

print(frase[0])
print(frase[:6])
print(frase[::2])

aux = len(frase)
print(aux)
aux = frase.count('o')
print(aux)
aux = frase.count('o', 0, 15)
print(aux)

aux = frase.find('Python') #Posição da ocorrência
print(aux)
aux = frase.find('Android')
print(aux)
aux = 'Estou' in frase #Retorna bool
print (aux)

aux = frase.replace('Python','Android')
print (aux)
aux = frase.upper()
print (aux)
aux = frase.lower()
print (aux)
aux = frase.capitalize() #Primeira fica em maisculo
print (aux)
aux = frase.title() #Todas as palavras recebem letras maísculas
print (aux)
frase.strip() #Remove espaços inúteis
frase.rstrip() #Espaços inuteis da direita
frase.lstrip() #Espaços inuteis da esquerda

frase.split() #Divide espaços
'-'.join(frase) #Substitui espaços
''' o codigo abaixo retornou uma string
o segundo codigo retornou uma classe _io
o terceiro codigo retornou um erro , nao consegui identificar
o quarto codigo leu todas as linhas porem o import json permaneceu inativo '''

#with open('db.json', 'r') as file:
#    print(file.read())

#with open('db.json', 'r') as file:
#    print(type(file))

#import json
#
#with open('db.json', 'r') as file:
#    print(type(json.loads(file.read())))

with open('db.json', 'r') as file:
    for linha in file.readlines():
        print(linha)

import json

words = ['choque de cultura',
         'tv quase',
         'historia cabeluda',
         'assim disse o joao',
         'luide verso',
         'fala MR',
         'Galas Feios',
         'desce a letra show',
         'ponto em comum',
         'ferrez']

with open('words_pt.json', 'w') as file:
    file.write(json.dumps(words))
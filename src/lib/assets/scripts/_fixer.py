import os 

pathos = 'src/lib/words'

listo = os.listdir(pathos)

for fillo in listo[:1]:
    if fillo != '.DS_Store':
        print(fillo)
        with open(f"{pathos}/{fillo}", 'r') as f:
            lines = f.readlines()
            # texto = '\n'.join(lines)
            # print(texto)
            # print(f.read())
            print(lines)

# print(listo)
# importing the module
import json

# reading the data from the file 
with open('file_poezii.txt') as f:
    data1 = f.read()
with open('file_alt_text.txt') as f:
    data2 = f.read()

js1 = json.loads(data1)
js2 = json.loads(data2)
suma=0
for cuv2 in js2.keys():
     if cuv2 in js1.keys():
          dif=js1[cuv2]-js2[cuv2]
     else:
         dif=js2[cuv2]
     if dif<0:
          dif=-dif
     suma+=dif
print(suma)
print(suma/len(js2.keys()))
#Afișați și media diferenței în modul (suma anterioară împărțită la numărul de cuvinte din fișier).????

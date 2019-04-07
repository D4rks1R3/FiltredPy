import re
import requests

url = "http://files.cedrotech.com/tickbytick/Bmf/20190109.log"
r = requests.get('http://127.0.0.1/logs.log')
t = str(r.text)
tex = 'tst.txt'

whi = open(tex,"w+")
whi.write(t)
whi.close()

def separador():
   file = open(tex, "r")
   ler = file.readlines()

#lê e separa as strings
   for i in ler:
      a = i.split("|", 1)
      f, b = a
      if f == "TF2Z99":
         fi = open("win.txt", "a+")
         fi.write(str(a)+'\n')
         fi.close()
      if f == "WDOG19":
         fj = open("wnd.txt", "a+")
         fj.write(str(a)+'\n')
         fj.close()
   file.close()
separador()


"""
def organizar_alfabeticamente(lista):
   "Organiza alfabeticamente as strings contidas dentro de uma lista."
   for x in range (len(lista)):
      
      for y in range (len(lista)):
         
         if lista[x] < lista[y]:
            lista[x], lista[y] = lista[y], lista[x]


lista = ["h", "g", "g",  "f"]
print ("Antes:", lista)
organizar_alfabeticamente(lista)
print ("Depois:", lista)
"""

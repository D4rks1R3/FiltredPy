import re
import requests
import time
tex = 'tst.txt'

def down():
   print('Inicio  >>', time.strftime('%H:%M:%S')+'\n')
   url = "http://files.cedrotech.com/tickbytick/Bmf/20190109.log"
   r = requests.get(url)
   t = str(r.text)
   tex = 'tst.txt'
   whi = open(tex,"a+")
   whi.write(t)
   whi.close()
   print("COMPLETO!")
   print("FIM >>", time.strftime('%H:%M:%S')+'\n')

def separador():
   file = open("tst.txt", "r")
   ler = file.readlines()
   for i in ler:
      a = i.split("|", 1)
      f, b = a
      if f == "WING19":
         fi = open("win.txt", "a+")
         fi.writelines(str(a)+'\n')
         fi.close()
      if f == "WDOG19":
         fj = open("wdg.txt", "a+")
         fj.writelines(str(a)+'\n')
         fj.close()

   file.close()

down()
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

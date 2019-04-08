#!/usr/bin/python3.6
import re
import requests
import time
tex = 'tst.txt'

def down():
   print('Inicio  >>', time.strftime('%H:%M:%S')+'\n')
   url = "http://files.cedrotech.com/tickbytick/Bmf/20190109.log"
   r = requests.get('http://127.0.0.1/logs.log')
   t = str(r.text)
   tex = 'tst.txt'
   whi = open(tex,"a+")
   whi.write(t)
   whi.close()
   print("COMPLETO!")
   print("FIM >>", time.strftime('%H:%M:%S')+'\n')

def separador():
   file = open("20190109.log", "r+")
   ler = file.readlines()
   for i in ler:
      a = i.split("|", 4)
      b = a[0:4]
      t, k = a[0:2]
        
      if t == 'WING19':
         print(b)
               
         fi = open("win.txt", "a+")
         fi.writelines(str(b)+'\n')
         fi.close()
         
      if t == 'WDOG19':
         print(b)
                  
         fj = open("wdg.txt", "a+")
         fj.writelines(str(b)+'\n')
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

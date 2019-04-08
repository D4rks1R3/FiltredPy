#!/usr/bin/python3.6
import re
import requests
import time
import os
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
   try:
       com = str(input("arquivo .log: "))   
       file = open(com, "r+")
       ler = file.readlines()
       for i in ler:
         a = i.split("|", 4)
         p, b, o, m  = a[0:4]
         tt = b.replace("-", ".")
         t, k = a[0:2]
         tr = t[0:3]
                  
         total = p[0:4]+","+tt+',,,'+o+','+m
        
         if tr == 'WIN':
               print(total)
               fi = open("win.txt", "a+")
               fi.writelines(str(total)+'\n')
               fi.close()
         
         if tr == 'WDO':
               print(total)          
               fj = open("wdo.txt", "a+")
               fj.writelines(str(total)+'\n')
               fj.close()

         file.close()
        
   except Exception as e:
         print("Erro encontrado!")
         os.system("pause")

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

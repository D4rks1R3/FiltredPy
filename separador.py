# -*- coding: utf-8 -*-
#!/usr/bin/python3

import glob
import requests
import time
import os
import platform


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

def comando():
    if platform.system() ==  "Windows":
          print("Filtragem terminada com sucesso")
          
    if platform.system() == "Linux":
          print("Filtragem terminada com sucesso")
          
          

arqu = str(input("Nome para Filtragem do primeiro: ")).upper()
arqd = str(input("Nome para Filtragem do segundo arquivo: ")).upper()

def separador():
   try:
      
      li = glob.glob("*.log")
      for i in li:
         print("lendo arquivo -->", i)
         time.sleep(1)
         ler = open(i, 'r+')
         lend = ler.readlines()
         for dd in lend:                
            a = dd.split("|", 4)
            p, b, o, m  = a[0:4]
            tt = b.replace("-", ".")
            t, k = a[0:2]
            tr = t[0:4]
            total = p[0:4]+","+tt+',,,'+o+','+m

            if arqu == " ":
               print("Preencha o primeiro campo!")
            if arqd == " ":
               print("Preencha o segundo campo")            
          
            if tr == arqu:
               print(total)
               fi = open(arqu+".txt", "a+")
               fi.writelines(str(total)+'\n')
               fi.close()
         
            if tr == arqd:
               print(total)          
               fj = open(arqd+".txt", "a+")
               fj.writelines(str(total)+'\n')
               fj.close()
            
            
      ler.close()
      comando()
            
   except Exception as e:
      print('erro:', e)
    
  

separador()

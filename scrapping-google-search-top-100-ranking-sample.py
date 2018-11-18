def pausa():
    tiempo1 = datetime.datetime.now()
    tiempo2 = random.randint(10,30)
    tiempof = tiempo1 + datetime.timedelta(0,0,1,0,tiempo2,0,0)
    x = 0
    while tiempo1 < tiempof:
        lim=random.randint(2000000,5000000)
        for tiempo in range(1,lim,1):
            tiempo2 = tiempo2 + 1
        tiempo1 = datetime.datetime.now()
		if x == 0 :
            corte = '*\n*Fin en medio de pausa' + str(datetime.datetime.now()) + ' \n*\n'
            print(corte)
			x = 1

import datetime
from bs4 import BeautifulSoup
import os
import os.path
import random
import re
import requests
#import MySQLdb
try:
    from urllib.parse import unquote
except:
    from urllib import unquote

#cdir = r'C:\Users\Sabrina\Documents\StayGoldSpa\code' # Directory of files txt .
cdir = r'/home/tnemexico/' # Directory of files txt .
#arch1 = cdir + '\\' + 'kwords-urls.txt'
#arch2 = cdir + '\\' + 'kwords-ranking.txt'
arch1 = cdir + 'kwords-urls.txt'
arch2 = cdir + 'kwords-ranking.txt'
#archivo_in  = open(arch1, 'r',encoding='UTF-8')
#archivo_out = open(arch2,'w+',encoding='UTF-8')
archivo_in  = open(arch1, 'r')
archivo_out = open(arch2,'w+')

corte = '*\n*Inicio Proceso ' + str(datetime.datetime.now()) + ' \n*\n'
archivo_out.write(corte)

#    &q=  &uule= delimitadores de la busqueda
limite1 = '&q='
limite2 = '&uule='
    
maxprocesos = random.randint(30,37)

busqueda = 'www.staygoldspa.com.ar'

separador = "\n\n*************************"

listaurls   = archivo_in.readlines()

encontradas = 0
procesos = 0

for url in listaurls:

    if procesos > maxprocesos :
        #delay
        procesos = 0
        corte = '*\n*Inicio Corte ' + str(datetime.datetime.now()) + ' \n*\n'
        archivo_out.write(corte)
        archivo_out.close()
        pausa()
        archivo_out = open(arch2,'a+')
        corte = '*\n*Fin corte' + str(datetime.datetime.now()) + ' \n*\n'
        archivo_out.write(corte)

    url = url.strip('\n')
    salida = ''
    cont = 1
    tiempo2 = 1
    limite =  random.randint(1000000,1999999)
    for tiempo in range(1,limite,1):
        tiempo2 = tiempo2 + 1
    r = requests.get(url)
    procesos = procesos + 1
    sopa = BeautifulSoup(r.text, 'html.parser')
    importes = re.findall(r'\$[0-9,.]+', r.text)
    etiquetas = re.findall(r'<h3 class="r">', r.text)
    resultados = sopa.find_all("h3", class_="r")
    #print( "LINK \n" , url )
    # obtener kword de la url de busqueda
    mach1 = url.find(limite1) + 3
    mach2 = url.find(limite2) 
    kword = url[mach1:mach2]
    kword = kword.replace('+','%20')
    palabra = unquote(kword) 
    #salida = palabra + '|' 
    #print( re.findall(r'\$[0-9,.]+', r.text))
    #print( re.findall(r'\$ [0-9,.]+', r.text))
    for resultado in resultados:
        #print( resultado )
        ri = resultado.contents
        xx = ri[0].get('href')
        if (xx.find(busqueda) > -1):
            salida = palabra + '|'
            salida = salida + str(cont) + '\n'
            archivo_out.write(salida)
            print( encontradas,  " -> Encontre ", palabra," en el lugar : ", cont)
            #print( xx )
            encontradas = encontradas + 1
        cont = cont + 1

final = "\n\n Total de Encontradas" + '|' + str(encontradas)
archivo_out.write(final)
print("\n\n Total de Encontradas", encontradas)

corte = '*\n*Fin de Proceso ' + str(datetime.datetime.now()) + ' \n*\n'
archivo_out.write(corte)

archivo_in.close()
archivo_out.close()


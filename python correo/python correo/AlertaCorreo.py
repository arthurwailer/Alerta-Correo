import smtplib
import os 
import platform
import subprocess
import time
from datetime import datetime
import telnetlib
import socket
import os
from random import randint
from time import strftime
from time import strptime
import threading
import sqlite3

def enviarCorreo(URL,hora_fecha):

    mensaje = URL + ' ' + 'DOES NOT TRANSMIT SINCE' + ' '+  hora_fecha 

    subject = URL + '  ' + 'DOES NOT RESPOND' 
    messaje = 'Subject: {}\n\n{}'.format(subject,mensaje)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('slopez@aikologic.com','silladeplata1234')
    list_mail = ['slopez@aikologic.com', 'sebastian.lopez.c@usach.cl']
    for mail in list_mail:
        print mail
        server.sendmail('slopez@aikologic.com',mail, messaje)
    server.quit()
    print 'correo enviado'

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    #print type(param), param 

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '2', host]
    #print type(command), command
    print "aqui se imprime el subprocces",subprocess.call(command)
    return subprocess.call(command) == 0

def leer():
    fic = open("contador.txt", "r")
    boleano = int(fic.read())
    return boleano
    fic.close()

def escribir(boleano):
    fic = open("contador.txt", "w")
    fic.write(str(boleano))
    fic.close()

def hora_fecha():
    now = datetime.now()
  
    return now

def telnet(HOST,PORT):
    try:
        tn = telnetlib.Telnet(HOST,PORT,3)
       

        print ("[!] Conectado a Servidor Telnet -> " + HOST + ":" + PORT)
        time.sleep(0.2)
        tn.close()
        return True

    except:
        print "not connect telnet"

        return False

def getContador(numero):
    conn = sqlite3.connect("DatosFs")
    if conn:

        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
            select contador from DatosFs
            where id = {0}'''.format(numero))
        contador = cursor.fetchone()[0]
        print contador
        return contador
    
        conn.commit()
        cursor.close()

def getUrl(numero):
    conn = sqlite3.connect("DatosFs")
    if conn:

        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
            select url from DatosFs
            where id = {0}'''.format(numero))
        url = cursor.fetchone()[0]
        print url
    
        conn.commit()
        cursor.close()


def Update(id,contador):
    conn = sqlite3.connect("DatosFs")
    if conn:
        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE DatosFs
        set contador = {1}
        where id = {0} '''.format(id,contador))
        conn.commit()
        cursor.close()
        conn.close()

#Update(1,0)

def update_fecha_hora(id,fecha_hora):
    conn = sqlite3.connect("DatosFs")
    if conn:
        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE DatosFs
        set fecha_hora_alarma = '{1}'
        where id = {0} '''.format(id,fecha_hora))
        conn.commit()
        cursor.close()
        conn.close()


def getDatetime(numero):
    conn = sqlite3.connect("DatosFs")
    if conn:

        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
            select fecha_hora_alarma from DatosFs
            where id = {0}'''.format(numero))
        datetime = cursor.fetchone()[0]
        datetime1 = str(datetime)
        
    
        conn.commit()
        cursor.close()
        return datetime1

def update_tiempo_offline(id,tiempo_offline):
    conn = sqlite3.connect("DatosFs")
    if conn:
        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE DatosFs
        set time_offline = '{1}'
        where id = {0} '''.format(id,tiempo_offline))
        conn.commit()
        cursor.close()
        conn.close()


# datetime_base_datos = getDatetime(1) # ya convertido a str

# print datetime_base_datos , type(datetime_base_datos)
# datetime_base_datos1 =  datetime.strptime(datetime_base_datos, '%Y-%m-%d %H:%M:%S.%f') #convierte a data time

# print type(datetime_base_datos1), datetime_base_datos1 #tipo data time
now = datetime.now() # hora actual
# tiempo_offline = datetime_base_datos1 - now # tiempo offline
# print "el tiempo ofline es, ", tiempo_offline
print type(now), now



conn = sqlite3.connect("DatosFs")
if conn:
    print "Connectado a la BBDD"
    cursor = conn.cursor()
    print "obteniendo tupla"
    cursor.execute("SELECT * FROM DatosFs")

    tables = cursor.fetchall()
    for rows in tables:
        id = rows[0]
        url = rows[1]
        fecha_hora_alarma = rows [2]
        time_offline = rows [3]
        contador = rows [4]
        print "id : ", id
        print "url ", url
        print "fecha_hora_alarma ", fecha_hora_alarma
        print "time_offline", time_offline
        print "contador: ", contador

        i = 0
        while i < 5:
            if telnet(url,'80'):
                 # escribe 1 en el block de notas
                print "hay coneccion telnet"
                i = i + 1
                if i == 5:
                    telnet(url,'80')
                    Update(id,1)
                    time.sleep(5)
                    break
            else:
                i = i + 1
                if i == 5:
                    now = datetime.now() # hora actual 
                    enviarCorreo(url,str(now))
                    Update(id,0)
                    datetime_base_datos = getDatetime(1) 
                    datetime_base_datos1 =  datetime.strptime(datetime_base_datos, '%Y-%m-%d %H:%M:%S.%f')
                    now = datetime.now()
                    tiempo_offline = datetime_base_datos1 - now
                    now1 = str(now)
                    print type(now1)
                    tiempo_offline1 = str(tiempo_offline)
                    print type(tiempo_offline1)
                    update_fecha_hora(id,now1)
                    update_tiempo_offline(id,tiempo_offline1)



                




        







# for URL in URL_lista:
#     print "url", URL
#     i = 0
#     while i < 5:
#         if telnet(URL,'80'):
#              # escribe 1 en el block de notas
#             print "hay coneccion telnet"
#             i = i + 1
#             if i == 5:
#                 telnet(URL,'80')
#                 escribir(1)
#                 time.sleep(5)
#                 break
#         else:
#             if leer() == 1 : # si es 1 es primera vez que se envia el correo 
#                 i = i + 1
               
#                 if i == 5 :
#                     now = datetime.now() # hora actual 
#                     enviarCorreo(URL,str(now))
#                     print "no hay telnet y se envia correo de alerta "
#                     time.sleep(5)
#                     escribir(0) # Escribe 0 en el block de notas
#                     break
                




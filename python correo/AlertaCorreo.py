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

def enviarCorreo(URL,hora_fecha,list_mail):
    mensaje = URL + ' ' + 'DOES NOT TRANSMIT SINCE' + ' '+  hora_fecha 
    subject = URL + '  ' + 'DOES NOT RESPOND' 
    messaje = 'Subject: {}\n\n{}'.format(subject,mensaje)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('slopez@aikologic.com','PASSWORD')
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
    command = ['ping', param, '1', host]
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
    format = now.strftime('%d-%m-%Y %H:%M Hour')
    print (format)
    return format
    

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

def tiempo_offline():

    now = datetime.now() # hora actual 
    datetime_base_datos = getDatetime(1) 
    datetime_base_datos1 =  datetime.strptime(datetime_base_datos, '%Y-%m-%d %H:%M:%S.%f') # cambia de dato a datetime.datetime
    now = datetime.now()
    now1 = str(now) # datetime a str
    tiempo_offline = now - datetime_base_datos1 # resta de datetime
    tiempo_offline1 = str(tiempo_offline)
    return tiempo_offline1

def getCont_segundo_mail(numero):
    conn = sqlite3.connect("DatosFs")
    if conn:
        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
            select contador_segundo_correo from DatosFs
            where id = {0}'''.format(numero))
        contador_segundo_correo = cursor.fetchone()[0]
        
    
        conn.commit()
        cursor.close()
        return contador_segundo_correo

def upd_segundo_mail(id,contador_segundo_correo):
    conn = sqlite3.connect("DatosFs")
    if conn:
        print "Connectado a la BBDD"
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE DatosFs
        set contador_segundo_correo = {1}
        where id = {0} '''.format(id,contador_segundo_correo))
        conn.commit()
#         cursor.close()
#         conn.close()


# telnet('mel.cl.trackit.host','80')
# telnet('cma.cl.trackit.host','80')
# telnet('200.6.102.247','80')
# telnet('192.168.123.1','80')
# telnet('192.168.122.1','80')


ping('192.168.121.1')


# list_mail_1 = ['slopez@aikologic.com']
# list_mail_2 = ['sebastian.lopez.c@usach.cl']


# conn = sqlite3.connect("DatosFs")
# if conn:
#     print "Connectado a la BBDD"
#     cursor = conn.cursor()
#     print "obteniendo tupla"
#     cursor.execute("SELECT * FROM DatosFs")

#     tables = cursor.fetchall()
#     for rows in tables:
#         id = rows[0]
#         url = rows[1]
#         fecha_hora_alarma = rows [2]
#         time_offline = rows [3]
#         contador = rows [4]
#         contador_segundo_correo = rows[5]
#         destinatario = rows[6]
#         print "id : ", id
#         print "url ", url
#         print "fecha_hora_alarma ", fecha_hora_alarma
#         print "time_offline", time_offline
#         print "contador: ", contador # boleano 0 y 1 flag
#         print "contador_segundo_correo",contador_segundo_correo
#         print "destinarario numero: ", destinatario


#         now = datetime.now() # hora actual 
#         now1 = str(now) # datetime a str
#         tiempo_actual = hora_fecha()
#         i = 0
#         j = 0
#         z = 0
#         while i < 5:
#             i = i + 1
#             if telnet(url,'80'):
#                  # escribe 1 en el block de notas
#                 print "hay coneccion telnet"
#                 z = z + 1
#                 time.sleep(2)
#                 if z == 5:
#                     telnet(url,'80')
#                     Update(id,1)
#                     time.sleep(2)
#                     upd_segundo_mail(id,0)
#                     update_tiempo_offline(id,str(0))
#                     update_fecha_hora(id,str(0))             
#             else:
#                 j = j + 1 
#                 time.sleep(2)
#                 if j == 5:
#                     if contador == 1:
#                         update_fecha_hora(id,tiempo_actual)
#                         update_tiempo_offline(id,str(0))
#                         #time_caida =tiempo_offline()
#                         Update(id,0)
#                         cont_mail2 = getCont_segundo_mail(id)
#                         cont_mail2 = cont_mail2 + 1
#                         upd_segundo_mail(id,cont_mail2)
                        
#                         if destinatario == 0:
#                             enviarCorreo(url,tiempo_actual,list_mail_1)
#                         else:
#                             enviarCorreo(url,tiempo_actual,list_mail_2)


#                     else:
#                         #tiempo_caido = tiempo_offline()
#                         #update_tiempo_offline(id,tiempo_caido)
#                         contador_segundo_correo = contador_segundo_correo + 1
#                         upd_segundo_mail(id,contador_segundo_correo)
#                         if contador_segundo_correo == 3:
#                             #time_caida =tiempo_offline()
#                             if destinatario == 0:
#                                 enviarCorreo(url,fecha_hora_alarma,list_mail_1)
#                             else:
#                                 enviarCorreo(url,fecha_hora_alarma,list_mail_2)

#                         else:
#                             print "no hace nada"









                




        









        







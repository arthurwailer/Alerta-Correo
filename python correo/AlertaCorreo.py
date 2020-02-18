import smtplib
import os 
import platform
import subprocess
import time
from datetime import datetime


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
    boleano
    return boleano
    fic.close()

def escribir(boleano):
    fic = open("contador.txt", "w")
    fic.write(str(boleano))
    fic.close()

def hora_fecha():

    now = datetime.now()
    now= str(now)
  
    return now




escribir(1)
print leer()


fecha_hora = hora_fecha()
print fecha_hora
URL_lista = ['192.168.100.25',]

for URL in URL_lista:
    print "url", URL

    i = 0
    while i < 2:
        if ping(URL):
             # escribe 1 en el block de notas
            print "hay ping"
            i = i + 1
            if i == 2:
                escribir(1)
                time.sleep(0.5)
                break
        else:
            if leer() == 1 : # si es 1 es primera vez que se envia el correo 
                i = i + 1
               
                if i == 2 :
                    enviarCorreo(URL,str(fecha_hora))
                    print "no hay ping y se envia correo de alerta "
                    time.sleep(5)
                    escribir(0) # Escribe 0 en el block de notas
                    break




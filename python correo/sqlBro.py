import sys
import telnetlib
import socket
import time
import os
from random import randint
from time import strftime
import threading

HOST = "cma.cl.trackit.host"
PORT = "80"

try:
	tn = telnetlib.Telnet(HOST,PORT,3)

	print ("[!] Conectado a Servidor Telnet -> " + HOST + ":" + PORT)
	time.sleep(0.2)
except:
	print "nose pudo conectar por telnet"

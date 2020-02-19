import sqlite3
import time 
import sys
import datetime 



# today = datetime.datetime.today()
# fechaHoraActual= today.today()
# print fechaHoraActual



#localtime = time.asctime( time.localtime(time.time()))
#cursor.execute("CREATE TABLE DatosFs(altura_raw REAL NOT NULL, fecha_hora_lectura_sensor VARCHAR(50) NOT NULL,  fecha_hora_recepcion VARCHAR(50) NOT NULL)")
def CrearTabla():
	conn = sqlite3.connect("DatosFs")
	if conn:
	    print "Connectado a la BBDD"
	    cursor = conn.cursor()
	    cursor.execute('''CREATE TABLE DatosFs(
	    	id INTEGER PRIMARY KEY,
	    	url varchar NOT NULL,
	    	fecha_hora_alarma varchar(50) NOT NULL,
	    	time_offline varchar(50) NOT NULL,
	    	contador int NOT NULL)''')
	    print "tabla creada "

	    
	    
def insertBBDD(url):
	try:
		conn = sqlite3.connect("DatosFs")
		if conn:
		    print "Connectado a la BBDD"
		    
		    cursor = conn.cursor()
		    
			
		            #angulo_roll = 20.6
		            #hora = (CURRENT_TIMESTAMP) 
		    print "insertando datos a la base de datos de lipigas"
		   #localtime = time.asctime( time.localtime(time.time()))
		    today = datetime.datetime.today()
		    fechaHoraActual= today.today()
		    contador = 0
		    consulta ='''INSERT INTO DatosFs(
		    url,
		    fecha_hora_alarma,
		    time_offline,
		    contador)
		    VALUES (?,?,?,?);'''
		    cursor.execute(consulta,(url,'2020-02-19 18:51:36.344000','2020-02-19 18:51:36.344000',contador))
		    print "datos insertados con exito"
	except Exception as e:
		print ("ocurrio un error al conectar a la BBDD",e)
	finally:
		conn.commit()
		cursor.close()
		conn.close()

def sql_fetch():
	try:
		conn = sqlite3.connect("DatosFs")
		cursor = conn.cursor()
		print "conectado"


		cursor.execute("SELECT contador from DatosFs")
		rows= cursor.fetchall()
		for row in rows:
			print row
		cursor.close()

		conn.close()
	except:
		print "Can't connet to BBDD"
		cursor.close()
		conn.close()

def alter():
	conn = sqlite3.connect("DatosFs")
	if conn:
		print "Connectado a la BBDD"
		cursor = conn.cursor()
		cursor.execute('''
		alter table DatosFs rename fecha_hora_alarma time''')
		cursor.close()

		conn.close()
		cursor.close()

		print "tabla creada "


insertBBDD('mel.cl.trackit.host')
#sql_fetch()
#insertBBDD('mel.cl.trackit.host')

#CrearTabla()
#altura_raw = 18.9
# fs = Fuelsensor_interface('192.168.100.187',5000)
# fs.connect()
# fs.get_app_version()
# altura_raw = fs.get_height()
# fs.get_pos()
# fs.close_socket()






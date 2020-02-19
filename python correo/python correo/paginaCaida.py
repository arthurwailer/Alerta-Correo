# -*- coding: UTF-8 -*-

 

import os

import pycurl

import sys

import shutil

import hashlib

 

# Lista que contiene las direcciones a revisar

files=[

	"http://cma.cl.trackit.host/",

	"http://mel.cl.trackit.host/",

]

 

def body(buf):

    global captureBody

    captureBody=captureBody+buf

 

## Callback function invoked when header data is ready

def header(buf):

    global captureHeader

    captureHeader=captureHeader+buf

 

def isOk(header):

	"""

	this function find in the header if exist the text "200 OK"

	"""

	for line in header.splitlines():

		if line.find("200 OK")>0:

			return True

	return False

 

for url in files:

	if url:

		print "------------------------"

		print url

		captureBody=""

		captureHeader=""

		c = pycurl.Curl()

		c.setopt(pycurl.URL, url)

		c.setopt(pycurl.WRITEFUNCTION, body)

		c.setopt(pycurl.HEADERFUNCTION, header)

		# Mostramos por pantalla toda la info para poder debugar el codigo

		# c.setopt(pycurl.VERBOSE, 1)

		c.perform()

		c.close()

 

		if isOk(captureHeader):

			fileName=url.split("/")[-1]

 

			# save the file

			f=file(fileName,"w")

			f.write(captureBody)

			f.close()

 

			# compare files

			if(os.path.exists(os.path.join(sys.path[0],"files",fileName))):

				print "exists"

				if hashlib.md5(file(fileName).read()).hexdigest()==hashlib.md5(file(os.path.join("files",fileName)).read()).hexdigest() and os.path.getsize(fileName)==os.path.getsize(os.path.join("files",fileName)):

					print "same"

				else:

					print "different"

					print "moved"

					shutil.move(fileName,os.path.join("files",fileName))

			else:

				print "Not exists"

				print "moved"

				shutil.move(fileName,os.path.join("files",fileName))

		else:

			print "Error download"
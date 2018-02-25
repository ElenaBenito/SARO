#!/usr/bin/python3

myfile = open('/etc/passwd', 'r')
lines = myfile.readlines()

interesantes = ['root', 'imaginario']

dicc = {}	#parte opcional2

for line in lines:
    datos = line.split(':')
#    print('USER: ' + datos[0] +' SHELL: '+ datos[-1][:-1])	#parte obligatoria
#	if datos[0] in interesantes:								#parte opcional1
#		print('USER: ' + datos[0] +' SHELL: '+ datos[-1][:-1])	#parte opcional1
	dicc[datos[0]] = datos[-1][:-1]		#parte opcional2

myfile.close()

#parte opcional2
print(dicc["root"])
try:
	print(dicc["imaginario"])
except KeyError: 
	print("imaginario no existe")

#otra opcional2/3:
#for usuario in interesantes
#	try:
#		print(usuario, "--->", dicc[usuario])
#	except KeyError:
#		print(usuario + "no existe")

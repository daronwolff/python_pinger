# -*- coding: utf-8 -*-
import os

#
# Clase para verificar  si las ips están en línea y limpiar la BD
#
class Pinger(object):
	
	#
	# Regresar IP
	#
	def get_ips(self):
		ips = ["192.168.151.124","192.168.151.1","192.168.151.254","192.168.23.12"]
		return ips

	#
	# Hacer ping
	#
	def do_list_ping(self):
		ips = self.get_ips()
		if len(ips)>0:
			for ip in ips:
				print "HACIENDO PING A "+str(ip)
				response = os.system("ping -c 1 " + ip)
				if response == 0:
					self.do_something(ip)
 				else:
 				  clear_ip(ip)
		print ips

	#
	# Quitar la IP de la bd
	#
	def clear_ip(self,ip):
		print "LA IP "+str(ip)+" ESTÁ ABAJO."
		return True

	#
	# No hace nada, pero podría hacerlo
	# 
	def do_something(self,ip):
		print "Toma un café con "+str(ip)
		return True

	def do_ping_simple(self,ip):
 		response = os.system("ping -c  " + ip)
		if response == 0:
			print "HOST CONECTADO"
			return True
		else:
			print "HOST NO CONECTADO"
			return False

pinger = Pinger()
pinger.do_list_ping()
#pinger.do_ping_simple("192.168.151.254")




		
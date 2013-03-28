#!/usr/bin/env python
from socket import * 
import threading
import sys
import datetime

#Global variables
num_threads = 100
open_ports = []
lock = threading.Lock()


def scan_port_range(min, max, target_ip):
	for i in range(min, max):
		s = socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((target_ip, i))
		
		#Add any open ports to the array	
		if(result == 0):
			lock.acquire() #Lock the array from access by other threads
			open_ports.append(i)
			lock.release() 
		s.close()

def print_results():
	open_ports.sort()
	for i in open_ports:
		print 'Port %d: OPEN' % (i,)

if __name__ == '__main__':
	max_port = 1025 #Highest port to scan
	target = sys.argv[1]
	target_ip = gethostbyname(target)
   	print 'Starting scan on host:', target_ip

    	#Time the scan
	#Start timer
	start = datetime.datetime.now()

	#scan reserved ports 20-max_port
   	for i in range(0, num_threads):
		#Determine next min and max port ranges to scan
		min = 20 + i * (max_port / num_threads)
		max = max_port if (i == num_threads - 1) else min + (max_port / num_threads) - 1
		#Spawn a new thread
		t = threading.Thread(target=scan_port_range, args=(min, max, target_ip))
		t.start()
	
	#Stop the timer
	elapsed_time = datetime.datetime.now() - start
	print_results()
	print '%d ports scanned in %d microseconds' % (max_port - 20, elapsed_time.microseconds)


#!/usr/bin/env python
from socket import * 
import threading
import sys

#Global variables
num_threads = 100

def scan_port_range(min, max, target_ip):
	for i in range(min, max):
		s = socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((target_ip, i))
		
		if(result == 0):
			print 'Port %d: OPEN' % (i,)
		s.close()

if __name__ == '__main__':
	max_port = 1025 #Highest port to scan
	target = sys.argv[1]
	target_ip = gethostbyname(target)
   	print 'Starting scan on host ', target_ip

    	#scan reserved ports 20-max_port
	#Special case: first min must start at 20
	scan_port_range(20, max_port / num_threads, target_ip)
   	for i in range(1, num_threads):
		#Determine next min and max port ranges to scan
		min = i * (max_port / num_threads) + 1
		max = max_port if (i == num_threads - 1) else min + (max_port / num_threads) - 1
		#Spawn a new thread
		t = threading.Thread(target=scan_port_range, args=(min, max, target_ip))
		t.start()

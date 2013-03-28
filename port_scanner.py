#!/usr/bin/env python
from socket import * 
import threading


def scan_port_range(min, max, target_ip):
	for i in range(min, max):
		s = socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((target_ip, i))
		
		if(result == 0):
			print 'Port %d: OPEN' % (i,)
		s.close()



if __name__ == '__main__':
    	target = raw_input('Enter host to scan: ')
    	targetIP = gethostbyname(target)
   	 print 'Starting scan on host ', targetIP

    	#scan reserved ports
   	for i in range(20, 1025, 100):
		

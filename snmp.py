#'''snmpd service discover scripts

from socket import *

from optparse import OptionParser

options = OptionParser(usage='%prog server [options]', description='snmp discover scripts')
options.add_option('-p', '--port', type='int', default=161, help='TCP port to test (default: 161)')


 
def h2bin(x):
    return x.replace(' ', '').replace('\n', '').decode('hex')

#snmp v3
data=h2bin('''
30 3e 02 01 03 30 11 02 
04 18 2e ef 88 02 03 00 
ff e3 04 01 04 02 01 03 
04 10 30 0e 04 00 02 01 
00 02 01 00 04 00 04 00 
04 00 30 14 04 00 04 00 
a0 0e 02 04 16 30 28 86 
02 01 00 02 01 00 30 00 
''')


def discover(ip,port):
	s =socket(AF_INET, SOCK_DGRAM)
	s.sendto(data,(ip,port))
	try:
		s.settimeout(5)
		string,addr=s.recvfrom(512)
		return string
	except:
		print "failure connecting to %s:%d" %(ip,port)
		quit()
	s.close()


if __name__=='__main__':
	opts,args=options.parse_args()
	if len(args)<1:
		options.print_help()
		quit()
	if(discover(args[0],opts.port)):
		print "snmpd service starting"
	else:
		print "snmpd service stoped"
	quit()

	
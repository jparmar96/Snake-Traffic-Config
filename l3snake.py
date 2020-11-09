from netaddr import *
#from arstCliLib import *
import sys
from netaddr import IPAddress
import netaddr
#dut = sys.argv[1]
#openSshOnDut( dut )
#setAccessMethod( dut, 'ssh' )

cmd = []
vlan_no = 3
count = 1
c = 0
vrf_no = 1

#This loop creates vrfs, enables ip and ipv6 routing for them

cmd.append ("ipv6 unicast-routing")
for i in range(1,33):
	cmd.append ("vrf definition %s" %i)
	cmd.append ("ip routing vrf %s" %i)
	cmd.append ("ipv6 unicast-routing vrf %s" %i)

#These two loops put interfaces in respective vrfs and give IP addresses to interfaces
ip = netaddr.IPNetwork('192.168.1.2/24')
for i in range(1,65):
	if i % 2 == 0:
		cmd.append("int et %s" %i + "/1")
		cmd.append("no switchport ")
		cmd.append("vrf forwarding %s" %vrf_no)
		cmd.append("ip address "  + str(ip.ip) + "/24")
		ip.value += 1
		vrf_no += 1
	if i % 2 == 1:
		cmd.append("int et %s" %(i) + "/1")
		cmd.append("no switchport ")
		cmd.append("vrf forwarding %s" %vrf_no)
		cmd.append("ip address "  + str(ip.ip) + "/24")
		ip.value += 255

#IPv4 static routes

ip = netaddr.IPNetwork('192.168.2.2/24')
for i in range(1,33):
	cmd.append("ip route vrf " + str(i) +  " 192.168.33.0/24 " + str(ip.ip))
	ip.value += 256

ip = netaddr.IPNetwork('192.168.32.1/24')
for i in range(32,0,-1):
	cmd.append("ip route vrf " + str(i) +  " 192.168.1.0/24 " + str(ip.ip))
	ip.value -= 256



#print cmd
cmdconfig = '\n'.join(cmd)
print (cmdconfig)
#sendCmd( dut, cmd, prompt='config' )

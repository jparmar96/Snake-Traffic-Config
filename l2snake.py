import sys
#from netaddr import IPAddress

#dut = sys.argv[1]
#openSshOnDut( dut )
#setAccessMethod( dut, 'ssh' )

cmd = []
vlan_no = 3
count = 1

for i in range(5,29):
	cmd.append("int et " + str (i) + "/1")
	if count == 1 or count == 2:
		cmd.append("switchport")
		cmd.append("switchport access vlan " + str(vlan_no))
		count += 1
		if count == 3:
			count = 1
			vlan_no += 1

for i in range(29,37):
	cmd.append("int et " + str (i) + "/1")
	if count == 1 or count == 2:
		cmd.append("switchport")
		cmd.append("switchport access vlan " + str(vlan_no))
		count += 1
		if count == 3:
			count = 1
			vlan_no += 1

"""
for i in range(49,55):
	cmd.append("int et %s/1 " %i)
	if count == 1 or count == 2:
		cmd.append("switchport access vlan " + str(vlan_no))
		count += 1
	if count == 3:
		count = 1
		vlan_no += 1
"""

cmdconfig = '\n'.join(cmd)
print(cmdconfig)
print("spanning-tree mode none")
#sendCmd( dut, cmd, prompt='config' )

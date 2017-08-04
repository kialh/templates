tnum = input("Introduce the ticket number (without TMC#): ")
desc = input("Enter the CR title: ")
interfaces = {'1': 'port1', '2': 'TMC-LAN', '3': 'TMC-Sectra', '4': 'TMC-RIS'}
count = 0
print("Available interfaces: ")
for i in interfaces.values():
	count += 1
	print ('{0}- {1}'.format(str(count),i))

sif = input("Select the source interface: ")
dif = input("Select the destination interface: ")
saddr = input("Source Address: ")
daddr = input("Destination Address: ")
action = ["ACCEPT", "DROP"]
print ("Available actions: ")
for a in action:
	print(a)
act = input("Select one action: ")
isnat = input("Is NAT needed (true or false): ")
log = {'1': 'No Log', '2': 'Log Security Events', '3': 'Log all sessions'}
count = 0
print("Logging options: ")
for j in log.values():
	count += 1
	print ('{0}- {1}'.format(str(count),j))
islog = input("Choose proper logging option: ")
services = input("Enter a list of services separated by comma: ")
template = '{0}{1}{2}- {3}{4}{5}{2}{6}{7}{2}{8}{9}{2}{10}{11}{2}{12}{13}{2}{14}{15}{2}{16}{17}{18}'.format("1) Log into the FortiManager with your windows credentials\n\
2) Lock the ADOM called EUROPE \n\
3) Go to Policy and Objects tab\n\
4) Create a new session with the following details:\n\
\t- This CR number\n\
\t- TMC#",tnum,"\n\t",desc,"\n5) Select the Policy Package called: bt1-fw8-root:\n\
6) Create a new policy with the following parameters: \n\
\t- Source Adddress: ",saddr,"- Destination Address: ",daddr,"- Source Interface: ",interfaces[sif],"- Destination Interface: ",interfaces[dif],"- Action: ",act,"- NAT: ",isnat,"- Logging options: ",log[islog],"\n\
7) Submit the session \n\
8) Lock the ADOM called EUROPE again \n\
9) Approve the session \n\
10) Perform an install wizard.")
print(template)
#with open("NewPolicy.txt","w") as fl:
#	fl.write(template)
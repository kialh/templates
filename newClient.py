tnum = input("Introduce the ticket number (without TMC#): ")
desc = input("Enter the CR title: ")
client = input("Write the new client: ")
address = input("Write the IP address of the client: ")
portele = input("Write the TCP port for elective channel: ")
portocb = input("Write the TCP port for on call BCN channel: ")
print(
"1) Log into the FortiManager with your own LDAP details.\n\
2) Lock the ADOM called Europe. \n\
3) Create a new session under Policy & Objects tab:\n\
\t - TMC#",tnum, "\n\
\t - New firewall object for ",client," and new policy to allow traffic from HSD\n\
4) Under Firewall Objects, click on Address.\n\
5) Create new.\n\
\t - Address name: ",client,"_HSD\n\
\t - Type: Subnet/IP Range\n\
\t - IP Range/Subnet: ",address, "\n\
\t - Interface: any. \n\
6) Now, create new Service under Firewall Objects: \n\
\t - Name: TCP_",portele,"\n\
\t - Protocol: TCP/UDP\n\
\t - IP/FQDN: 0.0.0.0\n\
\t - Source port: 1-65335\n\
\t - Destination port: ",portele,"-",portele,"\n\
7) Create another one for OCB channel: \n\
\t - Name: TCP_",portocb,"\n\
\t - Protocol: TCP/UDP\n\
\t - IP/FQDN: 0.0.0.0\n\
\t - Source port: 1-65335\n\
\t - Destination port:",portocb,"-",portocb,"\n\
8) Now it is time to create the policy. \n\
9) Select bt1-fw8_root policy package. \n\
10) Create new: \n\
\t - Source interface: port1\n\
\t - Source address: ",client,"_HSD\n\
\t - Destination interface: TMC-Sectra\n\
\t - Destination address: TMC-HSD2-PubNAT\n\
\t - Service: HSD, TCP_",portocb,", TCP_",portocb,"\n\
\t - Action: ACCEPT \n\
11) Submit the session \n\
12) Lock the ADOM called EUROPE. \n\
13) Approve the session \n\
13) Perform an install wizard under Policy & Objects tab \n\
")
tnum = input("Introduce the ticket number (without TMC#): ")
desc = input("Enter the CR title: ")
username = input("Write the username: ")
final = '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}'.format(
"1) Log into "
    "the FortiGate with tmc_emergency details (password stored in TPM) in Read-Write mode.\n\
2) Go to root Virtual Domain. Under User & Device list, choose User -> User definition. \n\
3) Search for ",username," and right-click on it. Revoke the token.\n\
4) Edit the account ",username," and assign him a new token.\n\
5) Send the activation code on the same step.\n\
6) Log out from the FortiGate.\n\
7) Perform a config retrieve in FortiManager: log in with your own details.\n\
\t - Lock the ADOM called EUROPE.\n\
\t - Under Device Manager tab, choose the bt1-fw8 Device.\n\
\t - Click on Revision History under \"Configuration and Installation Status\"\n\
\t - Click on Retrieve.\n\
\t - Edit the last Retrieve and write: ",desc,"- TMC#",tnum,"\n\
\t - Under Policy&Objects tab, create a session with following information: ",desc," - TMC",tnum," - Retrieve after creating and assigning a token to ",username,"\n\
\t - Under Device manager tab, choose the All Fortigate Device and Import Policy packages for root, market and CADaidence.\n\
\t - Submit the session.\n\
\t - Lock the ADOM called EUROPE again.\n\
\t - Approve the session.\n\
8) Log out from the fortimanager.")
print(final)
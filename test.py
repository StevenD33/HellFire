import os
import subprocess as sp


# allow_tcp_forwarding = sp.getoutput('grep -E AllowTcpForwarding /etc/ssh/sshd_config | head -1')
# permit_open = sp.getoutput('grep -E PermitOpen /etc/ssh/sshd_config')


# if allow_tcp_forwarding != "AllowTcpForwarding no"  :
#     if permit_open == "":
#         print("SSHD Config: AllowTcpForwarding has been explicitly set to something other than no, but no PermitOpen setting has been specified.\n This means any user that can connect to a shell or a forced-command based session that allows open port-forwarding, can port forward to any other accessible host on the network (authorized users can probe or launch attacks on remote servers via SSH port-forwarding and make it appear that connections are coming from this server).  Recommend disabling this feature by adding [AllowTcpForwarding no], or if port forwarding is required, providing a list of allowed host:ports entries with PermitOpen.  For example [PermitOpen sql.myhost.com:1433 mysql.myhost.com:3306]. ")
# else:
#     print(allow_tcp_forwarding)
#     print(permit_open)



sp.getoutput("chmod +x ./bash_script/authentication.sh")
sp.call("./bash_script/authentication.sh")

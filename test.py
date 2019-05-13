import os
import subprocess as sp


ssh_listen_address = sp.getoutput('grep -E "ListenAddress ::" /etc/ssh/sshd_config')

if ssh_listen_address == "#ListenAddress ::":
    print("SSHD Config: ListenAddress is set to default (all addresses).  SSH will listen on ALL available IP addresses.  Recommend change to a single IP to reduce the number of access points.  (Remember to restart SSHD with /etc/init.d/ssh restart after making changes)")
else:
    print(port_ssh)
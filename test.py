import os
import subprocess as sp


x11_forwarding = sp.getoutput('grep -E X11Forwarding /etc/ssh/sshd_config')


if x11_forwarding != "X11Forwarding no"  :
    print("SSHD Config: X11Forwarding should be set to no (unless needed).")
else:
    print(X11Forwarding)

strict_modes = sp.getoutput('grep -E StrictModes /etc/ssh/sshd_config')


if strict_modes != "StrictModes yes"  :
    print("SSHD Config: StrictModes should be set to yes (to check file permissions of files such as ~/.ssh, ~/.ssh/authorized_keys etc).")
else:
    print(strict_modes)



ignore_rhosts = sp.getoutput('grep -E IgnoreRhosts /etc/ssh/sshd_config')


if ignore_rhosts != "IgnoreRhosts yes"  :
    print("SSHD Config: IgnoreRhosts should be set to yes (this method of Authentication should be avoided).")
else:
    print(ignore_rhosts)

host_base_authentication = sp.getoutput('grep -E HostbasedAuthentication /etc/ssh/sshd_config')


if host_base_authentication != "HostbasedAuthentication no"  :
    print("SSHD Config: HostbasedAuthentication should be set to no (this method of Authentication should be avoided).")
else:
    print(host_base_authentication)

rhost_rsa_authentication = sp.getoutput('grep -E RhostsRSAAuthentication /etc/ssh/sshd_config')


if rhost_rsa_authentication != "RhostsRSAAuthentication no"  :
    print("SSHD Config: RhostsRSAAuthentication should be set to no (this method of Authentication should be avoided).")
else:
    print(rhost_rsa_authentication)

gateway_ports = sp.getoutput('grep -E GatewayPorts /etc/ssh/sshd_config')

if gateway_ports != ""  :
    print("SSHD Config: GatewayPorts is configured.  These allow listening on non-localhost addresses on the server.  This is disabled by default, but has been added to the config file.  Recommend remove this setting unless needed.")
else:
    print(gateway_ports)





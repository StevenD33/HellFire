import os
import subprocess as sp


x11_forwarding = sp.getoutput('grep -E X11Forwarding /etc/ssh/sshd_config')


if x11_forwarding != "X11Forwarding no"  :
    print("SSHD Config: X11Forwarding should be set to no (unless needed).")
else:
    print(X11Forwarding)

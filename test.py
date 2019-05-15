import os
import subprocess as sp


x11_forwarding = sp.getoutput('grep -E Protocol /etc/ssh/sshd_config')

print(x11_forwarding)
# if x11_forwarding != "X11Forwarding no"   :
#     print("SSHD Config: X11Forwarding should be set to no (unless needed).")
# else:
#     print(x11_forwarding)


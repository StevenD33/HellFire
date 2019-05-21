import subprocess as sp
import os.path




#subprocess.call("passwd -l root".split())
#print("root has been locked!")

#/etc/security/access.conf -:root: ALL EXCEPT LOCAL
#if os.path.exists("/etc/security/access.conf") == True:
#    with open("/etc/security/access.conf", "a") as myfile:
 #       myfile.write("\n-:root: ALL EXCEPT LOCAL")
#    print("access.conf edited!")
#else:
#    print("/etc/security/access.conf not found!")

#if os.path.exists("/etc/lightdm/lightdm.conf") == True:
#    with open("/etc/lightdm/lightdm.conf", "a") as myfile:
 #       myfile.write("\nallow-guest=false")
#
 #   print("guest locked!")
#else:
   # print("/etc/lightdm/lightdm.conf does not exist")

os.system("chmod +x ./bash_script/password.sh")
sp.call("./bash_script/password.sh")

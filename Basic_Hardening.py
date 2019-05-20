import subprocess


#BASIC UPGRADE
subprocess.call("apt-get update -y".split())
subprocess.call("apt-get upgrade -y".split())
subprocess.call("apt-get autoremove -y".split())
subprocess.call("apt-get autoclean -y".split())

important_services = ["openssh-server", "samba", "telnetd"] 

print("basic updates done! downloading tools!")

subprocess.call("apt-get install unattended-upgrades -y".split())
subprocess.call("dpkg-reconfigure -plow unattended-upgrades".split())
tools_array = ["libpam-cracklib", "nmap", "gufw", "rkhunter", "chkrootkit", "auditd", "clamtk"]
tools = "apt-get install " + ' '.join([str(x) for x in tools_array]) + " -y"
subprocess.call(tools.split())

#UPDATE FIREFOX
print("tools downloaded! updating firefox!")
subprocess.call("killall firefox".split())
subprocess.call("apt-get remove firefox -y".split())
subprocess.call("apt-get install firefox -y".split())

#RUN PROGRAMS
subprocess.call("software-properties-gtk".split())
subprocess.call("gufw")
subprocess.call("chkrootkit")
subprocess.call("auditctl -e 1".split())
#CONFIGURE ANTIVIRUS
subprocess.call("freshclam".split()) #updates antivirus definitions

#UPDATE DIST
print("updating dist....this may take a while")
subprocess.call("apt-get dist-upgrade -y".split())
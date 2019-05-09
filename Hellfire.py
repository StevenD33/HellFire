#!/bin/python

#function ctrl_c() {
#        echo "**You pressed Ctrl+C...Exiting"
#	exit 0;
#}

import os 

print ("################################################")
print ("################################################")
print ("################################################")

print ("_    _                 _          _ _ _   ")
print ("| |  (_)_ _ _  ___ __  /_\ _  _ __| (_) |_ ")
print ("| |__| |   \ || \ \ / / _ \ || / _  | |  _|")
print ("|____|_|_||_\_ _/_\_\/_/ \_\_ _\__ _|_|\__|") 
print ("###############################################")
print ("Welcome to security audit of your linux machine:")
print ("###############################################")
print ("Script will automatically gather the required info:")
print ("The checklist can help you in the process of hardening your system:")
print ("Note: it has been tested for Debian Linux Distro:")
os.system('sleep 3')
print ("###############################################")
print ("OK....$HOSTNAME..lets move on...wait for it to finish:")
os.system('sleep 3')
print ("Script Starts ;)")
os.system('START=$(date +%s)')
print  ("\e[0;33m 1. Linux Kernel Information////// \e[0m")
os.system('uname -a')
print ("###############################################")
print  ("\e[0;33m 2. Current User and ID information////// \e[0m")
os.system('whoami')
os.system('id')
print ("###############################################")
print ("\e[0;33m 3.  Linux Distribution Information///// \e[0m")
os.system('lsb_release -a')
print ("###############################################")
print  ("\e[0;33m 4. List Current Logged In Users///// \e[0m")
os.system('w')
print ("###############################################")
print -("\e[0;33m 5. $HOSTNAME uptime Information///// \e[0m")
os.system('uptime')
print ("###############################################")
print  ("\e[0;33m 6. Running Services///// \e[0m")
os.system('service --status-all |grep "+"')
print ("###############################################")
print  ("\e[0;33m 7. Active internet connections and open ports///// \e[0m")
os.system('netstat -natp')
print ("###############################################")
print  ("\e[0;33m 8. Check Available Space///// \e[0m")
os.system('df')
print ("###############################################")
print  ("\e[0;33m 9. Check Memory///// \e[0m")
os.system('free -h')
print ("###############################################")
print  ("\e[0;33m 10. History (Commands)///// \e[0m")
os.system('history')
print ("###############################################")
print -("\e[0;33m 11. Network Interfaces///// \e[0m")
os.system('ifconfig -a')
print ("###############################################")
print  ("\e[0;33m 12. IPtable Information///// \e[0m")
os.system('iptables -L -n -v')
print ("###############################################")
print ("\e[0;33m 13. Check Running Processes///// \e[0m")
os.system('ps -a')
print ("###############################################")
print ("\e[0;33m 14. Check SSH Configuration///// \e[0m")
os.system('cat /etc/ssh/sshd_config')
print ("###############################################")
print ("\e[0;33m 15. List all packages installed///// \e[0m")
os.system('apt-cache pkgnames')
print ("###############################################")
print ("\e[0;33m 16. Network Parameters///// \e[0m")
os.system('cat /etc/sysctl.conf')
print ("###############################################")
print ("\e[0;33m 17. Password Policies///// \e[0m")
os.system('cat /etc/pam.d/common-password')
print ("###############################################")
print ("\e[0;33m 18. Check your Source List file///// \e[0m")
os.system('cat /etc/apt/sources.list')
print ("###############################################")
print  ("\e[0;33m 19. Check for broken dependencies \e[0m")
os.system('apt-get check')
print ("###############################################")
print  ("\e[0;33m 20. MOTD banner message \e[0m")
os.system('cat /etc/motd')
print ("###############################################")
print ("\e[0;33m 21. List user names \e[0m")
os.system('cut -d: -f1 /etc/passwd')
print ("###############################################")
print ("\e[0;33m 22. Check for null passwords \e[0m")
users="$(cut -d: -f 1 /etc/passwd)"
for x in users:
    os.system('passwd -S $x |grep "NP"')
print ("###############################################")
print ("\e[0;33m 23. IP routing table \e[0m") 
os.system('route')
print ("###############################################")
os.system('END=$(date +%s)') 
os.system('DIFF=$(( $END - $START ))')
print ("Script completed in $DIFF seconds :")

print('END')

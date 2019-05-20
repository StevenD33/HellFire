import subprocess
import os.path


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

print('PASSWORD CONFIG')


# /etc/pam.d/common-password, /etc/pam.d/common-auth, and /etc/login.defs

subprocess.call("cp /etc/pam.d/common-password /etc/pam.d/common-password-backup".split())
subprocess.call("cp /etc/pam.d/common-auth /etc/pam.d/common-auth-backup".split())
subprocess.call("cp /etc/login.defs /etc/login_backup.defs".split())

print('read both files')
common_pass = open("/etc/pam.d/common-password","r+")
common_auth = open("/etc/pam.d/common-auth","r+")
login = open("/etc/login.defs","r+")



text = common_pass.read().strip("\n").split("\n")
print('remove potentially offending lines')
for i in range(len(text)):
    line = text[i]
    if ("password" in line) == True:
        text[i] = ""

text.append("password    [success=1 default=ignore]  pam_unix.so obscure use_authtok sha512 shadow remeber=5")
text.append("password    requisite           pam_cracklib.so retry=3 minlen=8 difok=3 reject_username minclass=3 maxrepeat=2 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1")
text.append("password    requisite           pam_pwhistory.so use_authtok remember=24 enforce_for_root")
text = '\n'.join([str(x) for x in text])
common_pass.seek(0)
common_pass.write(text)
common_pass.truncate()
common_pass.close()

print('EDITING common-auth')
text = common_auth.read().strip("\n").split("\n")
text.append("auth required pam_tally.so deny=5 unlock_time=900 onerr=fail audit even_deny_root_account silent")
text = "\n".join([str(x) for x in text])

common_auth.seek(0)
common_auth.write(text)
common_auth.truncate()
common_auth.close()

print('EDITING login')
text = login.read().strip("\n").split("\n")
for i in range(len(text)):
    line = text[i]
    if ("PASS_MIN_DAYS" in line) == True:
        text[i] = "PASS_MIN_DAYS 10"
    elif ("PASS_WARN_AGE" in line) == True:
        text[i] = "PASS_WARN_AGE 7"
    elif ("PASS_MAX_DAYS" in line) == True:
        text[i] = "PASS_MAX_DAYS 90"

text = "\n".join([str(x) for x in text])

login.seek(0)
login.write(text)
login.truncate()
login.close()

print('LOCK DOWN ON /etc/shadow')

subprocess.call("chmod o-r /etc/shadow".split())
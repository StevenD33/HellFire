import subprocess
import os.path


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

print("tools downloaded! updating firefox!")
subprocess.call("killall firefox".split())
subprocess.call("apt-get remove firefox -y".split())
subprocess.call("apt-get install firefox -y".split())

subprocess.call("software-properties-gtk".split())
subprocess.call("gufw")
subprocess.call("chkrootkit")
subprocess.call("auditctl -e 1".split())
subprocess.call("freshclam".split()) 

#UPDATE DIST
print("updating dist....this may take a while")
subprocess.call("apt-get dist-upgrade -y".split())


#/etc/security/access.conf -:root: ALL EXCEPT LOCAL
if os.path.exists("/etc/security/access.conf") == True:
    with open("/etc/security/access.conf", "a") as myfile:
        myfile.write("\n-:root: ALL EXCEPT LOCAL")
        print("access.conf edited!")
else:
    print("/etc/security/access.conf not found!")

if os.path.exists("/etc/lightdm/lightdm.conf") == True:
    with open("/etc/lightdm/lightdm.conf", "a") as myfile:
        myfile.write("\nallow-guest=false")

    print("guest locked!")
else:
    print("/etc/lightdm/lightdm.conf does not exist")


subprocess.call("crontab -l".split())




p = subprocess.Popen("ls /etc/cron*", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()
print (out)


p = subprocess.Popen("cat /etc/rc.local".split(), stdout=subprocess.PIPE)
output, err = p.communicate()
text = output

for line in text:
    if len(line) > 0 and line.strip(" ")[0] != "#" and line.strip(" ") != "exit 0" and line.strip(" ") != "":

        print("something is in /etc/rc.local ... you should check it out")


if os.path.exists("/etc/security/access.conf") == True:
    with open("/etc/security/access.conf", "a") as myfile:
        myfile.write("\n-:root: ALL EXCEPT LOCAL")
    print("access.conf edited!")
else:
    print("/etc/security/access.conf not found!")

if os.path.exists("/etc/lightdm/lightdm.conf") == True:
    with open("/etc/lightdm/lightdm.conf", "a") as myfile:
        myfile.write("\nallow-guest=false")

    print("guest locked!")
else:
    print("/etc/lightdm/lightdm.conf does not exist")
    def remove_malicous_software(malwares):
        attack = "apt-get purge " + ' '.join([str(x) for x in malwares]) + " -y"
        subprocess.call(attack.split())

    def bad(terms, directory):
        for term in terms:
            print("Searching for '{}'\n".format(term))
            found = subprocess.Popen(str("sudo find {} -iname {}".format(directory, term)).split(), stdout = subprocess.PIPE).stdout.readlines()
            if found != []:
                print("'{}' found in the following locations:\n".format(term))
                for item in found:
                    print(item)
                print("\n")

attack_array = ["at","netcat","wireshark","sipcrack","sucrack","john","hydra","ophcrack","tcpdump","whoopsie","at","gnome-games-common","gbrainy"]
remove_malicous_software(attack_array);


subprocess.call("apt-get autoremove -y".split())
subprocess.call("apt-get autoclean -y".split())

not_allowed = ["john","dsniff","tcpdump","*hydra*","*kismet*","*netcat*","*wireshark*","*crack*","*hack*","*keylog*","*malware*","*sniff*", "*jp*g","*JP*G","*.mp3","*.mp4","*.tiff"]
for item in not_allowed:
    bad([item], "/home")

subprocess.call("sysctl kernel.randomize_va_space=1".split())
subprocess.call("sysctl net.ipv4.conf.all.rp_filter=1".split())
subprocess.call("sysctl net.ipv4.conf.all.accept_source_route=0".split())

subprocess.call("sysctl net.ipv4.icmp_echo_ignore_broadcasts=1".split())
subprocess.call("sysctl net.ipv4.conf.all.log_martians=1".split())
subprocess.call("sysctl net.ipv4.conf.default.log_martians=1".split())

subprocess.call("sysctl -w net.ipv4.conf.all.accept_redirects=0".split())
subprocess.call("sysctl -w net.ipv6.conf.all.accept_redirects=0".split())
subprocess.call("sysctl -w net.ipv4.conf.all.send_redirects=0".split())
subprocess.call("sysctl kernel.sysrq=0".split())

subprocess.call("sysctl net.ipv4.tcp_timestamps=0".split())
subprocess.call("sysctl net.ipv4.tcp_syncookies=1".split())
subprocess.call("sysctl net.ipv4.icmp_ignore_bogus_error_responses=1".split())
subprocess.call("sysctl -p".split())

print("done!")

p = subprocess.Popen("lsb_release -r", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()



p = subprocess.Popen("dpkg --get-selections | grep -v deinstall", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()

installed = out


proc = subprocess.Popen("rm -rf /home/*/.ssh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, erro = proc.communicate()


subprocess.call("cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup".split())


if os.path.exists("/etc/ssh/sshd_config") == True:
    file = open("/etc/ssh/sshd_config","r+")
    text = file.read().strip("\n").split("\n")

    for i in range(len(text)):
        line = text[i]
        if ("PermitEmptyPasswords" in line) == True:
            text[i] = ""
        if ("PermitRootLogin" in line) == True:
            text[i] = ""
        if ("UsePrivilegeSeparation" in line) == True:
            text[i] = ""
        if ("SyslogFacility" in line) == True:
            text[i] = ""
        if ("LogLevel" in line) == True:
            text[i] = ""
        if ("LoginGraceTime" in line) == True:
            text[i] = ""
        if ("StrictModes" in line) == True:
            text[i] = ""
        if ("ChallengeResponseAuthentication" in line) == True:
            text[i] = ""
        if ("UsePAM" in line) == True:
            text[i] = ""
        if ("Protocol" in line) == True:
            text[i] = ""
        if ("DebianBanner" in line) == True:
            text[i] = ""
        if ("X11Forwarding" in line) == True:
            text[i] = ""
        if ("Protocol 2" in line) == True:
            text[i] = ""

    text.append("PermitEmptyPasswords no")
    text.append("PermitRootLogin no")
    text.append("UsePrivilegeSeparation yes")
    text.append("SyslogFacility AUTH")
    text.append("LogLevel INFO")
    text.append("LoginGraceTime 20")
    text.append("StrictModes yes")
    text.append("ChallengeResponseAuthentication yes")
    text.append("UsePAM yes")
    text.append("Protocol 2")
    text.append("DebianBanner no")
    text.append("X11Forwarding no")
    text.append("Protocol 1")


    text = '\n'.join([str(x) for x in text])

    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

    subprocess.call("sudo /etc/init.d/ssh restart".split())
else:
    print("/etc/ssh/sshd_config does not exist")

subprocess.call("ufw allow ssh".split())
subprocess.call("ufw allow http".split())
subprocess.call("ufw deny 23".split())
subprocess.call("ufw default deny".split())
subprocess.call("ufw enable".split())
subprocess.call("ufw limit OpenSSH".split())

subprocess.call("cp /etc/sysctl.conf /etc/sysctl_conf_backup".split())

if os.path.exists("/etc/sysctl.conf") == True:
    file = open("/etc/sysctl.conf","r+")
    text = file.read().strip("\n").split("\n")

    text.append("net.ipv4.tcp_syncookies = 1")

    text = '\n'.join([str(x) for x in text])
    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

    subprocess.call("sysctl -p".split())
else:
    print("/etc/sysctl.conf does not exist")

subprocess.call("sudo apt-get install vsftpd -y".split()) 
subprocess.call("cp /etc/vsftpd.conf /etc/vsftpd_backup.conf".split())

if os.path.exists("/etc/vsftpd.conf") == True:

    file = open("/etc/vsftpd.conf","r+")
    text = file.read().strip("\n").split("\n")

    for i in range(len(text)):
        line = text[i]
        if ("anonymous_enable" in line) == True:
            text[i] = ""
        if ("local_enable" in line) == True:
            text[i] = ""
        if ("write_enable" in line) == True:
            text[i] = ""
        if ("chroot_local_user" in line) == True:
            text[i] = ""


    text.append("anonymous_enable=NO")
    text.append("local_enable=YES")
    text.append("write_enable=YES ")
    text.append("chroot_local_user=YES")

    text = '\n'.join([str(x) for x in text])

    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

    subprocess.call("sudo /etc/init.d/vsftpd restart".split())
else:
    print("/etc/vsftpd.conf does not exist!")
append_only = [".bash_history",".bash_profile",".bash_login",".profile",".bash_logout",".bashrc"]
for appends in append_only:
    subprocess.call(("chattr +a ~/" + appends).split()) #set to append only
#if os.path.exists("~/.bashrc") == False:


#    subprocess.call("touch ~/.bashrc".split())

#text = file.read().strip("\n").split("\n")
#text.append("shopt -s histappend")
#text.append('readonly PROMPT_COMMAND="history -a" ')
#text.append("readonly HISTFILE")
#text.append("readonly HISTFILESIZE")
#text.append("readonly HISTSIZE")
#text.append("readonly HISTCMD")
#text.append("readonly HISTCONTROL")
#text.append("readonly HISTIGNORE")

text = '\n'.join([str(x) for x in text])
#file.seek(0)
#file.write(text)
#file.truncate()
#file.close()

subprocess.call("chmod 750 csh".split())
subprocess.call("chmod 750 tcsh ".split())
subprocess.call("chmod 750 ksh".split())


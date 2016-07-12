#!/usr/bin/python2
import getpass,os,commands,time
def func():
	os.system("dialog --inputbox 'Enter the name of the software' 10 30 2>  /root/Desktop/project/fentry.txt")
    	sfout=open('/root/Desktop/project/fentry.txt','r')
        key=sfout.read()
        sfout.close
	os.system('rpm -q '+key)
	time.sleep(2)
def func1():
	os.system("dialog --inputbox 'Software name' 10 30 2>  /root/Desktop/project/fentry.txt")
	sfout=open('/root/Desktop/project/fentry.txt','r')
        key1=sfout.read()
        sfout.close
	os.system('yum install '+key1)
	time.sleep(2)
def func2():
	while True:
		os.system(' dialog --menu "select one" 10 50 6  1 "Remove" 2 "Update" 3 "Search" 4 "Information about the package" 5 "See the installed packages" 6 "Exit" 2>/tmp/ch.txt ')
		fout1=open('/tmp/ch.txt')
		choice=fout1.read()
		fout1.close()
		if choice == '1':
			os.system("dialog --inputbox 'Software name' 10 30 2>  /root/Desktop/project/fentry.txt")
			sfout=open('/root/Desktop/project/fentry.txt','r')
        		key2=sfout.read()
        		sfout.close
			os.system('yum remove '+key2)
			time.sleep(2)			
		elif choice == '2':
			os.system("dialog --inputbox 'Software name' 10 30 2>  /root/Desktop/project/fentry.txt")
			sfout=open('/root/Desktop/project/fentry.txt','r')
        		key2=sfout.read()
        		sfout.close
        	        os.system('yum update '+key2)
			time.sleep(2)
		elif choice == '3':
			os.system("dialog --inputbox 'Software name' 10 30 2>  /root/Desktop/project/fentry.txt")
			sfout=open('/root/Desktop/project/fentry.txt','r')
        		key2=sfout.read()
        		sfout.close
			os.system('yum search all '+key2)
			time.sleep(4)
		elif choice == '4':
			os.system("dialog --inputbox 'Software name' 10 30 2>  /root/Desktop/project/fentry.txt")
			sfout=open('/root/Desktop/project/fentry.txt','r')
        		key2=sfout.read()
        		sfout.close
			os.system('yum info '+key2)
			time.sleep(2)
		elif choice == '5':
			os.system('yum list installed|less')
			time.sleep(2)
		elif choice == '6':
			break
while True:
	os.system(' dialog --menu "select one" 10 50 4  1 "Checking of the Software" 2 "Installation of the software" 3 "Operations on software" 4 "Exit" 2>/tmp/ch.txt ')
	sfout2=open('/tmp/ch.txt')
	choice=sfout2.read()
	sfout2.close()
	if choice == '1':
		func()
	elif choice == '2':
		func1()
	elif choice == '3':
		func2()
	elif choice == '4':
		break









	
	


	

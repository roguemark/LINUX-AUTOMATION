#!/usr/bin/python2
import os,commands,socket,getpass,time
def direc1():
	os.system("dialog --inputbox 'Enter the name of the Directory' 10 30 2>  /root/Desktop/project/fentry.txt")
	dout=open('/root/Desktop/project/fentry.txt','r')
	dir1=dout.read()
	dout.close
	os.system('mkdir '+dir1)
	os.system("dialog --infobox 'directory is successfully created' 10 30 ")
	time.sleep(2)
def direc2():
	os.system("dialog --inputbox 'Enter the name of the Directory' 10 30 2>  /root/Desktop/project/fdel.txt")
	dout=open('/root/Desktop/project/fdel.txt','r')
	dir2=dout.read()
	dout.close
	os.system('rmdir '+dir2)
	os.system("dialog --infobox 'directory is successfully deleted' 10 30 ")
	time.sleep(2)

while True:
	os.system(' dialog --menu "select one" 10 50 3  1 "Create a Directory" 2 "Remove a Directory" 3 "exit" 2>/tmp/ch.txt ')
	dout=open('/tmp/ch.txt')
	choice=dout.read()
	dout.close()
	if choice == '1':
		direc1()
	elif choice == '2':
		direc2()
	elif choice == '3':
		break


	


				
	
		
	

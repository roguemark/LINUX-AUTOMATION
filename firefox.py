#!/usr/bin/python2
import os,webbrowser,getpass,commands,socket,time
os.system('tput setaf 1 ')
def fox():
	os.system("dialog --inputbox 'Enter the Url' 10 30 2>  /root/Desktop/project/fentry.txt")
	frout1=open('/root/Desktop/project/fentry.txt','r')
	f1=frout1.read()
	frout1.close
	try:
		f2='http://www.'
		f3='.com'
		webbrowser.open_new_tab(f2+f1+f3)
	except console:
		os.system('dialog --infobox "Check your internet connection" 10 30')
		time.sleep(4)
def fox1():
	os.system("dialog --inputbox 'Enter what you want to search for:' 10 30 2>  /root/Desktop/project/fentry.txt")
	frout1=open('/root/Desktop/project/fentry.txt','r')
	lib=frout1.read()
	frout1.close
	try:
		ur="https://www.google.co.in/#q="
		urm="&gws_rd=cr"
		webbrowser.open_new(ur+lib+urm)
	except  :
		os.system('dialog --infobox "Check your internet connection" 10 30')
		time.sleep(1)
while True:
	os.system(' dialog --menu "select one" 10 50 3  1 "To open webpage of your choice" 2 "To search anything" 3 "exit" 2>/tmp/ch.txt ')
	frout1=open('/tmp/ch.txt')
	choice=frout1.read()
	frout1.close()
	if choice == '1':
		fox()
	elif choice == '2':
		fox1()
	elif choice == '3':
		break



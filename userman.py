#!/usr/bin/python2
import getpass,time,socket,commands,os
usr1=['humpher','kali','honey']
def users1():
	os.system('dialog --infobox "Create a user please" 10 30')
	time.sleep(2)
	os.system("dialog --inputbox 'Enter the name of the user' 10 30 2>/root/Desktop/project/fentry.txt")
	uout=open('/root/Desktop/project/fentry.txt','r')
	usr=uout.read()
	uout.close
	os.system('useradd  '+usr)
	ch=getpass.getpass('password')
	time.sleep(2)
	os.system('passwd '+usr)
	os.system('touch  '+usr)	
	uout = open('/root/Desktop/project/'+usr,'w')
	uout.write(ch)
	uout.close() 
	uout=open('/root/Desktop/project/userentry.txt','w')
      	usr1.append(usr)
   	uout.write("\n".join(map(lambda x: str(x), usr1)))
        uout.close()
	os.system('dialog --infobox "User is successfuly created" 10 30')
	time.sleep(2)
	os.system('dialog --infobox "Please login with newly created user" 10 30')
	time.sleep(1)
	os.system('su - '+usr)

def users2():
        os.system("dialog --inputbox 'Enter the name of the user' 10 30 2>/root/Desktop/project/fentry.txt")
	uout1=open('/root/Desktop/project/fentry.txt','r')
        usr2=uout1.read()
        uout1.close	
	if  usr2 in usr1:
			uout1=open('/root/Desktop/project/'+usr2,'r')
			usr3=uout1.read()
			uout1.close
			os.system('dialog --infobox "The password for your user is" 10 30')
			time.sleep(1)
			print usr3
			os.system('su - '+usr2)
			time.sleep(2)
			
	else:
			os.system('dialog --infobox "Please first create a user on yur system" 10 30')
def users3():
	os.system("dialog --inputbox 'Enter the name of the user' 10 30 2>/root/Desktop/project/fdel.txt")
        uout2=open('/root/Desktop/project/fdel.txt','r')
        usr4=uout2.read()
	if usr4 in usr1:
			os.system('rm -f  '+usr4)
			usr1.remove(usr4)
			os.system('dialog --infobox "Your entry on my list is removed" 10 30')
		 	print usr1
			time.sleep(2)
			f = open("/root/Desktop/project/userentry.txt")
			output=[]
			f.seek(0)
			for i in f:
				 if not usr4 in i:
       					  output.append(i)
			f.close()
			f = open("/root/Desktop/project/userentry.txt",'w')
			f.writelines(output)
			f.close()
			os.system('dialog --infobox "your user from my database is also removed" 10 30')
			os.system('userdel -r '+usr4)
			
	else:
			os.system('dialog --infobox "No such user is present" 10 30')
def users4():
	os.system("dialog --inputbox 'Enter the name of the group' 10 30 2>/root/Desktop/project/fentry.txt")
	uout3=open('/root/Desktop/project/fentry.txt','r')
        usr5=uout3.read()
        uout3.close
	os.system('groupadd '+usr5)
	time.sleep(2)
def users5():
	os.system("dialog --inputbox 'Enter the name of the group' 10 30 2>/root/Desktop/project/fdel.txt")
        uout3=open('/root/Desktop/project/fdel.txt','r')
        usr5=uout3.read()
        uout3.close
	os.system('groupdel '+usr5)
	time.sleep(2)

while True:
	os.system(' dialog --menu "select one" 10 50 3  1 "Login with a new user" 2 "Login with existing user" 3 "Remove a User" 4 "Create a group" 5 "Delete a group" 6 "exit" 2>/tmp/ch.txt ')
	fout1=open('/tmp/ch.txt')
	choice=fout1.read()
	fout1.close()
	if choice == '1':
		users1()
	elif choice == '2':
		users2()
	elif choice == '3':
		users3()
	elif choice == '4':
		users4()
	elif choice == '5':
		users5()
	elif choice == '6':
		break




	

#!/usr/bin/python2
import os,commands,socket,getpass,time
def disk1():
	os.system('clear')
	os.system('fdisk -l')
	time.sleep(2)

def disk2():
	os.system("dialog --inputbox 'enter name of the device to create partition' 10 30 2>  /root/Desktop/project/fentry.txt")
	fout=open('/root/Desktop/project/fentry.txt','r')
	dik2=fout.read()        
	fout.close
	dik3='sda'
	if dik2 == dik3:
		os.system('dialog --infobox "permission denied..Please insert your own harddisk" 10 30')
		time.sleep(2)	
	else:
		os.system('fdisk  /dev/'+dik2)
def disk3():
	os.system("dialog --inputbox 'enter name of the device to format' 10 30 2>  /root/Desktop/project/fentry1.txt")
        fout1=open('/root/Desktop/project/fentry1.txt','r')
        dik4=fout1.read()
        fout1.close 
        dik3='sda'
        if dik4 == dik3:
                os.system('dialog --infobox "permission denied..Please format your own harddisk" 10 30')
                time.sleep(2)
	else:
		os.system('mkfs.ext4  /dev/'+dik4)
def disk4():
	os.system("dialog --inputbox 'enter the name of the directory in media' 10 30 2>  /root/Desktop/project/fentry.txt")
	fout3=open('/root/Desktop/project/fentry.txt','r')
        dik6=fout3.read()
        fout3.close
	os.system('mkdir  /media/'+dik6)
	os.system("dialog --inputbox 'enter name of the device to mount' 10 30 2>  /root/Desktop/project/fentry.txt")
	fout2=open('/root/Desktop/project/fentry.txt','r')
	dik5=fout2.read()
        fout2.close 
        dik3='sda'
	if dik5==dik3:
		os.system('dialog --infobox "permission denied..Please mount your own harddisk" 10 30')
                time.sleep(2)
	else:
		os.system('mount /dev/'+dik5+'\t\t/media/'+dik6)


while True:
	os.system(' dialog --menu "select one" 10 60  5  1 "See all the available partitions" 2 "Create|delete your partition" 3 "format" 4 "mount your new partition" 5 "exit" 2>/tmp/ch.txt ')
	fout4=open('/tmp/ch.txt')
	choice=fout4.read()
	fout4.close()
	if choice == '1':
		disk1()
	elif choice == '2':
		disk2()
	elif choice == '3':
		disk3()
	elif choice == '4':
		disk4()
	elif choice == '5':
		break




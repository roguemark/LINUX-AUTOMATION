#!/usr/bin/python2
import os,commands,getpass,time
def lvm1():
	os.system('clear')
	os.system('fdisk -l')
	time.sleep(2)
	os.system('dialog --infobox "check into the partition table for assigning  the Physical Volume Group" 10 50')
	os.system("dialog --inputbox 'Enter the name of the 1 Physical Volume Group' 10 30 2>  /root/Desktop/project/fentry.txt")
        lout=open('/root/Desktop/project/fentry.txt','r')
        lv1=lout.read()
        lout.close 
	os.system("dialog --inputbox 'Enter the name of the 2  Physical Volume Group' 10 30 2>  /root/Desktop/project/fentry1.txt")
        lout=open('/root/Desktop/project/fentry1.txt','r')
        lv2=lout.read()
        lout.close
	lv3='sda'
	if lv1 == lv3 and lv2 == lv3:
		os.system('dialog --infobox "Permission denied" 10 50')
	else:
		os.system('pvcreate /dev/'+lv1)
		os.system('pvcreate /dev/'+lv2)
		os.system('pvdisplay')
		time.sleep(5)
		os.system('dialog --infobox "Physical volume is created " 10 50')
		os.system("dialog --inputbox 'Enter the name of the Volume group to be made' 10 30 2>  /root/Desktop/project/fentry2.txt")
		lout=open('/root/Desktop/project/fentry2.txt','r')
     	        lv4=lout.read()
                lout.close
		os.system('vgcreate  '+lv4+'/dev/'+lv1+'  /dev/'+lv2)
		os.system('vgdisplay '+lv4)
		time.sleep(3)
		os.system('dialog --infobox " Volume group is created " 10 50')
		os.system("dialog --inputbox 'Enter the name of the logical group to be made' 10 30 2>  /root/Desktop/project/fentry3.txt")
		lout=open('/root/Desktop/project/fentry2.txt','r')
                lv5=lout.read()
                lout.close
		os.system('lvcreate --name '+lv5+' --size -2G'+lv4)
		os.system('lvdisplay')
		time.sleep(3)
		os.system('dialog --infobox " Logical Volume group is created " 10 50')
		time.sleep(2)
		os.system('dialog --infobox " Time to Format " 10 50')
		time.sleep(2)
		os.system('mkfs.ext4  /dev/'+lv4+'/'+lv5)
		os.system('dialog --infobox " Preparing to Mount " 10 50')
		time.sleep(2)
		os.system('mkdir  /media/newvolume1')
		os.system('mount  /dev/'+lv4+'/'+lv5+'  /media/newvolume1')
	        os.system('dialog --infobox " process  completed " 10 50')
def lvm2():
		lout1=open('/root/Desktop/project/fentry2.txt','r')
                lv6=lout1.read() 
                lout1.close
		lout1=open('/root/Desktop/project/fentry3.txt','r')
                lv7=lout.read()
                lout1.close
		os.system('lvextend --size +1G /dev/'+lv6+'/'+lv7)
		time.sleep(4)
		
while True:
	os.system(' dialog --menu "select one" 10 50 3  1 "TO do lvm management" 2 "Extending lvm size only after it is created" 3 "exit" 2>/tmp/ch.txt ')
	lout2=open('/tmp/ch.txt')
	choice=lout2.read()
	lout2.close()
	if choice == '1':
		lvm1()
	elif choice == '2':
		lvm2()
	elif choice == '3':
		break
	


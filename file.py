#!/usr/bin/python2
import os,commands,time,socket,getpass

fil3 = ['access','fentry','firefox','software','test',
'access','file2','firefox','directory','file','project','start']
def file1():
	os.system("dialog --inputbox 'Enter the name of the file' 10 30 2>  /root/Desktop/project/fentry.txt")
	fil1=open('/root/Desktop/project/fentry.txt','r')
	fil2=fil1.read()
	fil1.close
	fout = open('/root/Desktop/project/filentry.txt','w')
	fout.write("\n".join(map(lambda x: str(x), fil3)))
	fout.close() 
	if fil2 in fil3:
		os.system('dialog --infobox "file already exists" 10 30')
		time.sleep(2)
	else:
		fout=open('/root/Desktop/project/filentry.txt','w')
      	        fil3.append(fil2)
   	        fout.write("\n".join(map(lambda x: str(x), fil3)))
		print fil3
                fout.close()
		os.system('touch\t'+fil2)
		os.system('cp\t'+fil2+'\t  /root/Desktop')
		os.system('dialog --infobox "file is created" 10 30')
                time.sleep(2)
		print fil3

def file2():
	os.system("dialog --inputbox 'Enter the name of the file' 10 30 2>  /root/Desktop/project/fdel.txt")
        fout2=open('/root/Desktop/project/fdel.txt','r')
        fout3=fout2.read()
        fout2.close 
	if fout3 in fil3:
		 os.system('dialog --infobox "Wait for some time..." 10 30')
                 time.sleep(2)
		 os.system('rm -f '+fout3)   
		 os.system('dialog --infobox "file is deleted" 10 30')
                 time.sleep(2)                                  
		              
	else:
		os.system('dialog --infobox "File does not exists" 10 30')

while True:
	os.system(' dialog --menu "select one" 10 50 3  1 "Create a file" 2 "Remove a file" 3 "exit" 2>/tmp/ch.txt ')
	fout1=open('/tmp/ch.txt')
	choice=fout1.read()
	fout1.close()
	if choice == '1':
		file1()
	elif choice == '2':
		file2()
	elif choice == '3':
		break




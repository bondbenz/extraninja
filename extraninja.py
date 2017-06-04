#!/usr/bin/python
#! Email Combo Extractor
import os,platform



if platform.system()=='Windows':
  os.system('cls')
else:
  os.system('clean')

print '''
                                       
         _               _       _     
 ___ _ _| |_ ___ ___ ___|_|___  |_|___ 
| -_|_'_|  _|  _| .'|   | |   | | | .'|
|___|_,_|_| |_| |__,|_|_|_|_|_|_| |__,|
                              |___|    
       Email:pass Combo email extractor
       WWW.TWIN.NINJA 
       CODE by BONDBENZ                      
      '''

combo = raw_input("[+] Combo email:pass file : ")
lines = open(combo, 'r').readlines()
print '[!] Working ...'
for line in lines:
    elem = line.split(':')
    email = elem[0].strip()
    with open('twinninja.txt', 'a') as myfile:
			 myfile.write(email)
			 myfile.write('\n')
print '[+] File generated as : twinninja.txt'

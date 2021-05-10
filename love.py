#Love Calculator

import os
os.system('clear')
col = '\033[1;95m'

logo = '''

                          .---.._ 
       ......__         .'       \._     __...... 
     /         \       /      <) :  \   /         \ 
    /          /      |           __.|  \          \ 
   /          (       )          (       )          \
  /            \_   _/            \_   _/            \
 / (             '''                '''             ) \
  (((           /   /              \   \           ))) 
 (()))    (    ((  ((    \    /    ))  ))    )    ((())
 (((())   ))  (()) \ \   ))  ((   / / (())  ((   (())))
)(())(( (( )) ))(( ))(( ((    )) ))(( ))(( ((FinnO)(())(

Just For Fun
'''
print col+logo

user = 'Omar'
password = 'Raj'

while True :
	us = raw_input('Enter Tools User: ')
	if us==user:
		print 'Correct Username'
		passs = raw_input('Enter Tools Password: ')
		if passs==password:
			print'Correct Password\nWelcome To Love World'
			break
		else:
			print 'Wrong Password'
	else:
		print ' Wrong Username'
		os.system('xdg-open https://www.facebook.com/Black.B.07/')
print'please wait...'
import time,os
time.sleep(2)
os.system('clear')
col = '\033[1;95m'
logo = ''' 
_
  ___  _ __ ___   __ _ _ __   _ __ __ _ (_)
 / _ \| '_ ` _ \ / _` | '__| | '__/ _` || |
| (_) | | | | | | (_| | |    | | | (_| || |
 \___/|_| |_| |_|\__,_|_|    |_|  \__,_|/ |
                                      |__/
'''
print col+logo
import time,os,random
FN = 'Liza' , 'Anisa' , 'Meda' , 'Lamia' , 'Fatema' , ' Habiba' , 'Sultana' , 'Runa' , 'Maisa' , 'Lota' , 'Nipu' , 'Rusa' , 'Rusu' , 'Nazma' , ' Mansura' , 'Nadi' , 'Nadia' , 'Rumi' , 'Farida' , 'Ruzi' , 'Somaiya' , 'Tamima' , 'Marufa' , 'Tamanna' , 'Taiyeba'
MN = 'Abir' , 'Samir' , 'Adil' , ' Mohsin' , 'Akash' , 'Rakib' , 'Mehebub' , 'Tanzil' , 'Hasan' , 'Omar Raj' , 'Sojol' , 'Sojon' , 'Rahat' , 'Momin' , 'Navid' , 'Abid' , 'Shihan' , 'Rony' , 'Sifat' , 'Rifat'
col = '\033[1;92m'
logo = '''
1.Male
2.Fimale
'''
print col+logo
t =input('Select Your Gender: ')

if t==1:
  print 'You are A Male'
  raw_input('Enter Your Name: ')
  time.sleep(5)
  print 'Your Lover Name: '
  print random.choice(FN)

elif t==2:
  print 'You Are A Fimale'
  raw_input('Enter Your Name: ')
  time.sleep(5)
  print 'Your Lover Name: '
  print random.choice(MN)
  
else:
  print '\033[1;91mWrong Number'
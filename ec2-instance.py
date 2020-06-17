#!/usr/bin/python3

import list_ec2
import time
import os

import boto3
ec2 = boto3.resource('ec2')

#curses library supplies a terminal-independent screen-painting and keyboard-handling
import curses 
                          
menu = ['List EC2 instances', 'Start EC2 instance', 'Stop EC2 instance', 'Validate connection']

# *************** function to print (menu) on the center of the screen **********************
def print_menu(stdscr,selected_row_idx):
 stdscr.clear()                          #clear screen
 h,w = stdscr.getmaxyx()                 #get height and width of screen

 for idx, row in enumerate(menu):
  x = w//2 - len(row)//2
  y = h//2 - len(menu)//2 + idx 
  if idx == selected_row_idx:
   stdscr.attron(curses.color_pair(1))   
   stdscr.addstr(y,x,row)
   stdscr.attroff(curses.color_pair(1))
  else:
   stdscr.addstr(y,x,row)

 stdscr.refresh()


# *********************** function to perform the selected operation *************************
def switch(stdscr,i):
 if i==0:
  for instance in ec2.instances.all():
   stdscr.addstr(1,0,"Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(instance.id,     instance.platform,instance.instance_type, instance.public_ip_address, instance.image.id, instance.state))
 if i==1:
  try:
   ec2.Instance('i-0d6fc11a8fc37f60c').start()
   stdscr.addstr(1,0,"Started EC2 instance with id i-0cd7f6a42bfbf9995.")
   os.system('ssh -i "aish.pem" ubuntu@ec2-100-25-168-230.compute-1.amazonaws.com')
  except Exception as e:
   print(e)
		
  
 if i==2:
  ec2.Instance('i-0d6fc11a8fc37f60c').stop()
  stdscr.addstr(1,0,"Started EC2 instance with id i-0cd7f6a42bfbf9995.")
 
 if i==3:
  stdscr.addstr(1,0,os.system('ssh -i "aish-keypair.pem" ubuntu@ec2-100-25-168-230.compute-1.amazonaws.com'))

 if i==4:
  stdscr.addstr(1,0,os.system('ping 172.31.44.4'))


  


# ********************************* main function *******************************************
def main(stdscr):
 curses.curs_set(0)
 curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
 current_row_idx = 0
 print_menu(stdscr, current_row_idx)
 while 1:
  key = stdscr.getch()
  stdscr.clear()
  if key == curses.KEY_UP and current_row_idx>0:
   current_row_idx-=1
  elif key == curses.KEY_DOWN and current_row_idx<len(menu)-1:
   current_row_idx+=1
  elif key == curses.KEY_ENTER or key in [10,13]:
   stdscr.addstr(0,0,"You pressed {} ".format(menu[current_row_idx]))
   switch(stdscr, current_row_idx)
   stdscr.refresh()
   stdscr.getch()
   if current_row_idx == len(menu) - 1:
    break
  print_menu(stdscr, current_row_idx)
  stdscr.refresh()

curses.wrapper(main)

#!/bin/python3
W="\x1b[1;37m"#White
R="\x1b[0;32m" #red
B="\x1b[1;34m" #blue
P="\x1b[0;35m" #Purple
C="\x1b[0;36m" #cyan
G="\x1b[1;32m" #Green
Y="\x1b[0;33m" #Yellow


from N4Tools.Design import Color
from os import *
from random import *
co = Color()
clr = system("clear")
def log():
	print(""" 
	┌┬┐┌─┐┌─┐┬  ┬┌─┬┌┬┐  ┬ ┬
         │ │ ││ ││  ├┴┐│ │───└┬┘
         ┴ └─┘└─┘┴─┘┴ ┴┴ ┴    ┴   
	 """)
log()
h = "\x1b[0;32mNote :- \x1b[0;31mPlease Enter 'help' to show options ."
print(h)
while True:
	root = input ("""\x1b[0;32mA7Y\x1b[0;36m@\x1b[0;31mTOOLS \x1b[0;35m*/\x1b[0;33m$ """)
	if root == "help":
		print("""
	\x1b[1;30m1. Games
	
	• snack game : Good Game
	• rg : random game
	
	\x1b[1;34m2. Network
	
	• full_net : Full Network Check.
	• cyop : Check Your Open Ports.
	• chep : Check Network Open Ports.
	• ax : Aggressive Examination.
	• kr: Knowing The Router's Operating System.
	
	\x1b[1;36m3.websites
	
	• host : Know Host Any Websites.
	• who : Info For Any Websites.
	
	\x1b[1;32m4. System
	
	• c : Clear
	• exit : Exit From The Tool.
	• banner : Show Banner Of The Tool.
	• update : Update Your Os.
	• upgrade : Upgrade Your Os.
	• v_os : Show Version Your Os (Linux).
	
	\x1b[1;35m5. About
	
	• about : Show About Of The Codder.
	• v : Version Of The Tool.
	• team : Show Info For My Team.
	• ch : Show My Channel Youtube.
	• telg : Show My User Telegram.
	
	\x1b[1;37m6. Updating
	
	• aupdate : Update The Tool.
	• aupgrade : Upgrade The Tool.
	
	\x1b[0;31mNote :- \x1b[0;32mCodded By Sfx And Thanks Allah.
	
	""")
	if root == "rg":
		rand = randint(0,10)
		clear = system("clear")
		log()
		usr = input("Hi,Enter Your User :- ")
		print ("welcome, "+usr)
		num = input("Enter Any Number : ")
		if rand == num :
			print (rand)
			print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			print ("Random Number Is ^^^ ")
			win = "You Are The Winer, "+usr
			print (win)
		else:
			print (rand)
			print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			print ("Random Number Is ^^^ ")
			lose = "You Are The Loser, "+usr
			print (lose)
			print ("Good Luck ... ")
	if root == "full_net":
		system("clear")
		log()
		print (" checking ..... ")
		system("nmap 192.168.1.*")
		print ("Good Bye ^_^ ")
	if root == "cyop":
		system("clear")
		log()
		ipp = input("Enter Your Ip :- ")
		print ("your ip is : "+ipp)
		system("nmap --open "+ipp)
		print ("Good Bye ^_^ ")
	if root == "chep":
		system("clear")
		log()
		y = input("Enter Your Ip :- ")
		print ("your ip is :- ")
		v = input ("Enter Check Port :- ")
		system("nmap -p "+v+" "+y)
		print ("Good Bye ^_^ ")
	if root == "ax":
		system("clear")
		log()
		h = input("Enter Your Ip :- ")
		system("nmap "+h+" "+"-A")
		print ("Good Bye ^_^ ")
	if root == "kr":
		system("clear")
		log()
		gate = input("Enter Your Gateway :- ")
		system("nmap -O "+gate)
		print ("Good Bye ^_^ ")
	if root == "host":
		import socket
		import sys
		system("clear")
		log()
		hist = input("Enter Your Target : ")
		ip = socket.gethostbyname(hist)
		print ("Your Target Is :- "+hist)
		print ("Host Your Target Is :- "+ip)
		print ("Good Bye ^_^ ")
	if root == "who":
		system("clear")
		log()
		piw = input("Enter Your Target :- ")
		system("whois "+piw)
		print ("Good Bye ^_^ ")
	if root == "c":
		system("clear")
		user = input("Enter Your User :- ")
		system("clear")
		print("Welcome In Your Home, "+user)
	if root == "exit":
		system("clear")
		log()
		system("exit")
	if root == "banner":
		system("clear")
		log()
	if root == "update":
		system("clear")
		log()
		system("sudo apt-get update -y")
		print("Good Bye ^_^ ")
	if root == "upgrade":
		system("clear")
		log()
		system("sudo apt-get upgrade -y")
		print("Good Bye ^_^ ")
	if root == "about":
		system("clear")
		log()
		print ("My Name :- Sam ")
		print ("Name My Team :- A.7.Y Team")
		print ("Name Codder :- Mr. Sfx")
		print ("Good Bye ^_^ ")
	if root == "v":
		system("clear")
		log()
		print ("Version This Tool :- 1.0 ")
		print("Good Bye ^_^ ")
	if root == "team":
		system("clear")
		log()
		print ("Name Of The Team :- A.7.Y Team")
		print ("Contry :- AL ARAB")
		print ("Admin User :- @AL_Alamy ")
		print("Good Bye ^_^ ")
	if root == "ch":
		system("clear")
		log()
		system("bash ch.sh")
		print("Good Bye ^_^ ")
	if root == "telg":
		system("clear")
		log()
		system("bash telg.sh")
		print("Good Bye ^_^ ")
	if root == "aupdate":
		system("clear")
		log()
		system("sudo apt-get update -y")
		print("The Tool Has Been Update ... ")
		print ("Good Bye ^_^ ")
	if root == "aupgrade":
		system("clear")
		log()
		print("The Tool No Upgrade ... ")
		print ("Good Bye ^_^ ")
	if root == "v_os":
		system("clear")
		log()
		system("cat /etc/os-release")
		print("Good Bye ^_^ ")
root1 = input ("""\x1b[0;32mA7Y\x1b[0;36m@\x1b[0;31mTOOLS \x1b[0;35m*/\x1b[0;33m$ """)
if root1 == "rg":
	rand = randint(0,10)
	clear = system("clear")
	log()
	usr = input("Hi,Enter Your User :- ")
	print ("welcome, "+usr)
	num = input("Enter Any Number : ")
	if rand == num :
		print (rand)
		print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print ("Random Number Is ^^^ ")
		win = "You Are The Winer, "+usr
		print (win)
	else:
		print (rand)
		print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print ("Random Number Is ^^^ ")
		lose = "You Are The Loser, "+usr
		print (lose)
		print ("Good Luck ... ")
if root1 == "full_net":
	system("clear")
	log()
	print (" checking ..... ")
	system("nmap 192.168.1.*")
	print ("Good Bye ^_^ ")
if root1 == "cyop":
	system("clear")
	log()
	ipp = input("Enter Your Ip :- ")
	print ("your ip is : "+ipp)
	system("nmap --open "+ipp)
	print ("Good Bye ^_^ ")
if root1 == "chep":
	system("clear")
	log()
	y = input("Enter Your Ip :- ")
	print ("your ip is :- ")
	v = input ("Enter Check Port :- ")
	system("nmap -p "+v+" "+y)
	print ("Good Bye ^_^ ")
if root1 == "ax":
	system("clear")
	log()
	h = input("Enter Your Ip :- ")
	system("nmap "+h+" "+"-A")
	print ("Good Bye ^_^ ")
if root1 == "kr":
	system("clear")
	log()
	gate = input("Enter Your Gateway :- ")
	system("nmap -O "+gate)
	print ("Good Bye ^_^ ")
if root1 == "host":
	import socket
	import sys
	system("clear")
	log()
	hist = input("Enter Your Target : ")
	ip = socket.gethostbyname(hist)
	print ("Your Target Is :- "+hist)
	print ("Host Your Target Is :- "+ip)
	print ("Good Bye ^_^ ")
if root1 == "who":
	system("clear")
	log()
	piw = input("Enter Your Target :- ")
	system("whois "+piw)
	print ("Good Bye ^_^ ")
if root1 == "c":
	system("clear")
	user = input("Enter Your User :- ")
	system("clear")
	print("Welcome In Your Home, "+user)
if root1 == "exit":
	system("clear")
	log()
	system("exit")
if root1 == "banner":
	system("clear")
	log()
if root1 == "update":
	system("clear")
	log()
	system("sudo apt-get update -y")
	print("Good Bye ^_^ ")
if root1 == "upgrade":
	system("clear")
	log()
	system("sudo apt-get upgrade -y")
	print("Good Bye ^_^ ")
if root1 == "about":
	system("clear")
	log()
	print ("My Name :- Sam ")
	print ("Name My Team :- A.7.Y Team")
	print ("Name Codder :- Mr. Sfx")
	print ("Good Bye ^_^ ")
if root1 == "v":
	system("clear")
	log()
	print ("Version This Tool :- 1.0 ")
	print("Good Bye ^_^ ")
if root1 == "team":
	system("clear")
	log()
	print ("Name Of The Team :- A.7.Y Team")
	print ("Contry :- AL ARAB")
	print ("Admin User :- @AL_Alamy ")
	print("Good Bye ^_^ ")
if root1 == "ch":
	system("clear")
	log()
	system("bash ch.sh")
	print("Good Bye ^_^ ")
if root1 == "telg":
	system("clear")
	log()
	system("bash telg.sh")
	print("Good Bye ^_^ ")
if root1 == "aupdate":
	system("clear")
	log()
	system("sudo apt-get update -y")
	print("The Tool Has Been Update ... ")
	print ("Good Bye ^_^ ")
if root1 == "aupgrade":
	system("clear")
	log()
	print("The Tool No Upgrade ... ")
	print ("Good Bye ^_^ ")
if root1 == "v_os":
	system("clear")
	log()
	system("cat /etc/os-release")
	print("Good Bye ^_^ ")
root2 = input ("""\x1b[0;32mA7Y\x1b[0;36m@\x1b[0;31mTOOLS \x1b[0;35m*/\x1b[0;33m$ """)
if root2 == "rg":
	rand = randint(0,10)
	clear = system("clear")
	log()
	usr = input("Hi,Enter Your User :- ")
	print ("welcome, "+usr)
	num = input("Enter Any Number : ")
	if rand == num :
		print (rand)
		print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print ("Random Number Is ^^^ ")
		win = "You Are The Winer, "+usr
		print (win)
	else:
		print (rand)
		print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print ("Random Number Is ^^^ ")
		lose = "You Are The Loser, "+usr
		print (lose)
		print ("Good Luck ... ")
if root2 == "full_net":
	system("clear")
	log()
	print (" checking ..... ")
	system("nmap 192.168.1.*")
	print ("Good Bye ^_^ ")
if root2 == "cyop":
	system("clear")
	log()
	ipp = input("Enter Your Ip :- ")
	print ("your ip is : "+ipp)
	system("nmap --open "+ipp)
	print ("Good Bye ^_^ ")
if root2 == "chep":
	system("clear")
	log()
	y = input("Enter Your Ip :- ")
	print ("your ip is :- ")
	v = input ("Enter Check Port :- ")
	system("nmap -p "+v+" "+y)
	print ("Good Bye ^_^ ")
if root2 == "ax":
	system("clear")
	log()
	h = input("Enter Your Ip :- ")
	system("nmap "+h+" "+"-A")
	print ("Good Bye ^_^ ")
if root2 == "kr":
	system("clear")
	log()
	gate = input("Enter Your Gateway :- ")
	system("nmap -O "+gate)
	print ("Good Bye ^_^ ")
if root2 == "host":
	import socket
	import sys
	system("clear")
	log()
	hist = input("Enter Your Target : ")
	ip = socket.gethostbyname(hist)
	print ("Your Target Is :- "+hist)
	print ("Host Your Target Is :- "+ip)
	print ("Good Bye ^_^ ")
if root2 == "who":
	system("clear")
	log()
	piw = input("Enter Your Target :- ")
	system("whois "+piw)
	print ("Good Bye ^_^ ")
if root2 == "c":
	system("clear")
	user = input("Enter Your User :- ")
	system("clear")
	print("Welcome In Your Home, "+user)
if root2 == "exit":
	system("clear")
	log()
	system("exit")
if root2 == "banner":
	system("clear")
	log()
if root2 == "update":
	system("clear")
	log()
	system("sudo apt-get update -y")
	print("Good Bye ^_^ ")
if root2 == "upgrade":
	system("clear")
	log()
	system("sudo apt-get upgrade -y")
	print("Good Bye ^_^ ")
if root2 == "about":
	system("clear")
	log()
	print ("My Name :- Sam ")
	print ("Name My Team :- A.7.Y Team")
	print ("Name Codder :- Mr. Sfx")
	print ("Good Bye ^_^ ")
if root2 == "v":
	system("clear")
	log()
	print ("Version This Tool :- 1.0 ")
	print("Good Bye ^_^ ")
if root2 == "team":
	system("clear")
	log()
	print ("Name Of The Team :- A.7.Y Team")
	print ("Contry :- AL ARAB")
	print ("Admin User :- @AL_Alamy ")
	print("Good Bye ^_^ ")
if root2 == "ch":
	system("clear")
	log()
	system("bash ch.sh")
	print("Good Bye ^_^ ")
if root2 == "telg":
	system("clear")
	log()
	system("bash telg.sh")
	print("Good Bye ^_^ ")
if root2 == "aupdate":
	system("clear")
	log()
	system("sudo apt-get update -y")
	print("The Tool Has Been Update ... ")
	print ("Good Bye ^_^ ")
if root2 == "aupgrade":
	system("clear")
	log()
	print("The Tool No Upgrade ... ")
	print ("Good Bye ^_^ ")
if root2 == "v_os":
	system("clear")
	log()
	system("cat /etc/os-release")
	print("Good Bye ^_^ ")

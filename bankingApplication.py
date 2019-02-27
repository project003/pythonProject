from array import *
import mysql.connector
import sys
class bank:

	bankname = "SBI"	
	
	print("Welcome to ",bankname)
		
	def deposit(self,amt,uname):
		'''deposit option'''
		dep="""update bank set balance = balance+%s where ename = %s"""
		data=(amt,uname)
		mycursor.execute(dep,data)
		mydb.commit()
		print("Amount deposited successfully")
	def withdraw(self,amt,uname):
		'''Withdraw option'''
		mycursor.execute("select balance from bank where ename =%s ",(uname,))
		chkBalance=mycursor.fetchall()
		for e in chkBalance:
			if amt<e[0]:
				mycursor.execute("update bank set balance = balance-%s where ename=%s",(amt,uname))
				print("Amount withdraw successfully")
			else:
				print("Insufficient Fund")
	def balanceCheck(self,uname):
		'''Balance check option'''
		mycursor.execute("select balance from bank where ename = %s ",(uname,))
		chkBalance=mycursor.fetchall()
		for e in chkBalance:
			print("Balance for user : ",uname," is ",e[0])

mydb = mysql.connector.connect(host="localhost",user="root",password="gaurav",database="bankDB")
mycursor=mydb.cursor()

b=bank()
choice = ''
balace = '' 

while True:
	'''Choices for customer'''
		
	print("1.Create new account\n2.Banking")
	option = int(input("Please select the banking method : "))
	def createAccount():
		'''creating new account'''
		
		name = input("Enter your name : ")
		city= input("city : ")
		age = int(input("age : "))
		balance = int(input("balance to deposite : "))
		insert=insert="""insert into bank(ename,age,city,balance) values(%s,%s,%s,%s)"""
		data=(name,age,city,balance)
		mycursor.execute(insert,data)
		mydb.commit()
		print("Account created successfully...")
		
	def banking():
		i=1
		'''checking if customer is authorised'''
		uname = input("Please enter your name : ")
		choice=''
		update="""select ename from bank where ename = %s"""
		mycursor.execute(update,(uname,))
		result=mycursor.fetchall()
		for row in result:
			print(row[0])
			if(uname==row[0]):
				while True:
					print("D-Deposit\nW-Withdraw\nB-Balance Check\nm-Main menu\nE-exit")
					choice=input("Please enter your choice : ")
					if choice=="d" or choice=="D": 
						amt=int(input("Enter amount to be deposited :  "))
						b.deposit(amt,uname)
					elif choice=="w" or choice=="W":
						amt=int(input("Enter amount to withdraw : "))
						b.withdraw(amt,uname)
					elif choice=="b" or choice=="B":
						b.balanceCheck(uname)
					
					elif choice=="e" or choice=="E":
						print("Thank you for banking with us...")
						sys.exit()
					elif choice=="m" or choice=="M":
						break	
					else:
		
						if i<3:
							'''Three wrong attempts allowed'''
							print("Wrong attempt : ",i)
							print("please enter valid choice")
							i+=1
						else:
							'''After max wrong attempts terminating session'''
							print("SORRY!!! max wrong attempts. Terminating session")
							sys.exit()
					
		if(choice!='m' or result == ''):
			print("unauthrised user")
				
	dictionary = {
				1:createAccount,
				2:banking
				}	
	dictionary.get(option)()
mydb.close()
from array import *
import sys
class bank:
	bankname = "SBI"	
	
	
	print("Welcome to ",bankname)
	
		
	def deposit(self,amt,j):
		'''deposit option'''
		
		balance[j] = balance[j]+amt 
		print("Amount deposited successfully")
	def withdraw(self,amt,j):
		'''Withdraw option'''
		if amt<balance[j]:
			balance[j] = balance[j]+amt
			print("Amount withdraw successfully")
		else:
			print("Insufficient Fund")
	def balanceCheck(self,j):
		'''Balance check option'''
		print("Balance for user : ",name[j],"is ",balance[j])
	
balance = array('i',[])	
b=bank()
name=[]
city=[]
age = array('i',[])
account=array('i',[])
while True:
	'''Choices for customer'''
		
	print("1.Create new account\n2.Banking")
	option = int(input("Please select the banking method : "))
	def createAccount():
		'''creating new account'''
		
		n = input("Enter your name : ")
		name.append(n)
		c = input("city : ")
		city.append(c)
		ag = int(input("age : "))
		age.append(ag)
		bal = int(input("balance to deposite : "))
		balance.append(bal)
		
	def banking():
		j=0
		k=0
		i=1
		
		'''checking if customer is authorised'''
		uname = input("Please enter your name : ")
		choice=''
		for e in range(len(name)):
			if name[k] == uname:
				j=k
				print(j)
				while True:
			
					print("D-Deposit\nW-Withdraw\nB-Balance Check\nm-Main menu\nE-exit")
					choice=input("Please enter your choice : ")
					if choice=="d" or choice=="D": 
						amt=int(input("Enter amount to be deposited :  "))
						b.deposit(amt,j)
		
					elif choice=="w" or choice=="W":
						amt=int(input("Enter amount to withdraw : "))
						b.withdraw(amt,j)
					elif choice=="b" or choice=="B":
						b.balanceCheck(j)
					
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
				
			k+=1
		if(choice!='m' or choice == ''):
			print("Name is unauthrised")
				
	dictionary = {
				1:createAccount,
				2:banking
				}	
	dictionary.get(option)()
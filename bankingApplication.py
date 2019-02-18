import sys

class banking:
	print("Welcome to SBI")
	
	def __init__(self,name,balance=0):
		self.name = name
		self.balance = balance
		
	def deposit(self,amt):
		self.balance = self.balance+amt
		print("Balance after deposit",self.balance)
	def withdraw(self,amt):
		if amt<self.balance:
			self.balance=self.balance-amt
			print("Balance after Withdraw",self.balance)
		else:
			print("Insufficient Fund")
	
name=input("Enter your name\n")
b=banking(name)
while True:
	print("D-Deposit\nW-Withdraw\nE-exit")
	choice=input("Please enter your choice")
	if choice=="d" or choice=="D": 
		amt=float(input("Enter amount to be deposited"))
		b.deposit(amt)
		
	elif choice=="w" or choice=="W":
		amt=float(input("Enter amount to withdraw"))
		b.withdraw(amt)
		
	elif choice=="e" or choice=="E":
		sys.exit()
	else:
		print("please enter valid choice")
		
		
		
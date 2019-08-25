from collections import OrderedDict
from config_file import database
from passlib.hash import argon2
from peewee import *
import cryptography.fernet
import datetime
import base64
import keyboard
import os
import re

class Display():
	"""Display output"""
	def __init__(self):
		pass
	def createNewDply(serName, useName, pasWord, grpItem):
		cls()
		print("\n")
		print("+{0:-^118}+".format(""))
		print("|{0:^118}|".format("New Account"))
		print("+{0:-^16}+{1:-^40}+{2:-^40}+{3:-^19}+".format("","","",""))
		print("|{0:^16}|{1:^40}|{2:^40}|{3:^19}|".format("Service Name","User Name","Password","Group Item"))
		print("+{0:-^16}+{1:-^40}+{2:-^40}+{3:-^19}+".format("","","",""))
		print("|{0:^16}|{1:^40}|{2:^40}|{3:^19}|".format(serName, useName, pasWord, grpItem))
		print("+{0:-^16}+{1:-^40}+{2:-^40}+{3:-^19}+".format("","","",""))
	def displayAccounts():
		cls()
		print("\n")
		print("+{0:-^124}+".format(""))
		print("|{0:^124}|".format("Display Accounts"))
		print("+{0:-^20}+{1:-^10}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
		print("| {0:<19}|{1:^10}| {2:<39}| {3:<19}| {4:<29}|".format("Service Name","Serial","User Name","Group Item","Date Time Group"))
		print("+{0:-^20}+{1:-^10}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
	def displayTitle(name):
		print("\n")
		print("+{0:-^30}+".format(""))
		print("|{0:^30}|".format(name))
		print("+{0:-^30}+".format(""))

def cls():
	"""Clears the CMD Line"""
	os.system('CLS')

def enc(pasWord):
	"""Encrypt password using a secret word"""
	while True:
		try:
			pasEncrypt = str(input("\nEnter a secret word to encrypt the password: "))
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			if pasEncrypt:
				hashKey = argon2.using(rounds=100).hash(pasEncrypt)
				# key encryption process
				hashKeyParam = re.split("[, $]", hashKey)
				passValue = (pasEncrypt+hashKeyParam[6][:-6]).zfill(32)
				del pasEncrypt #--------------> Removes the refernce object from the script 
				del hashKeyParam #--------------> Removes the refernce object from the script
				encodeHash = base64.urlsafe_b64encode(passValue.encode('utf-8'))
				del passValue #--------------> Removes the refernce object from the script
				encVal = cryptography.fernet.Fernet(encodeHash)
				# result of encryption
				password = encVal.encrypt(pasWord.encode('utf-8'))
				del encVal #--------------> Removes the refernce object from the script
				cls()
				print("[MESSAGE] Password succesfully encrypted")
				return hashKey, password
			else:
				print("[ERROR] Please enter a password")
				continue
		except ValueError:
			cls()
			print("[ERROR] The password must be less than 16 characters long")
			break
		except EOFError:
			cls()
			print("[ERROR] Invalid Entry")
			break

def denc(Id):
	"""Decrypt password using secret word"""
	try:
		keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
		query = database.select(Id)
		for entry in query:
			hashKeyParam = re.split("[, $]", entry.hashKey)
			print("\nSerial: ",entry.id)
			print("Service Name: ",entry.serviceName)
			print("User Name: ",entry.userName)
			print("Group Item: ",entry.groupItem)
			print("Password: ",str(entry.password)[2:-1])
			print("Hashkey: ",hashKeyParam[6]+hashKeyParam[7])
			print("Date Time Group: ",str(entry.dtg))
		while True:
			selection = str(input("\nDo you wish to decrypt password?\nPress [Y] to continue [N] to go back to main menu: "))
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			if selection == "y":
				pasEncrypt = str(input("\nEnter the secret word to decrypt the password: "))
				keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
				if pasEncrypt:
					for entry in query:
						# key encryption process
						result = argon2.verify(pasEncrypt,entry.hashKey)
						if result == True:
							hashKeyParam = re.split("[, $]", entry.hashKey)
							passValue = (pasEncrypt+hashKeyParam[6][:-6]).zfill(32)
							del hashKeyParam #--------------> Removes the refernce object from the script
							del pasEncrypt #--------------> Removes the refernce object from the script
							encodeHash = base64.urlsafe_b64encode(passValue.encode('utf-8'))
							del passValue #--------------> Removes the refernce object from the script
							encVal = cryptography.fernet.Fernet(encodeHash)
							# result of encryption
							password = encVal.decrypt(entry.password)
							del encVal #--------------> Removes the refernce object from the script
							cls()
							print("\nDecrypted Password: ", str(password)[2:-1])
							del password #--------------> Removes the refernce object from the script
						elif result == False:
							cls()
							print("[ERROR] Incorrect Password. Please try again.")
					break
				else:
					print("[ERROR] Please enter a password and try again.")
					continue
			elif selection == "n":
				cls()
				break
			else:
				print("[ERROR] Incorrect selection. Please select [Y] or [N].")
				continue
	except EOFError:
		cls()
		print("[ERROR] Invalid Entry.")
	except:
		cls()
		print("[ERROR] Invalid Entry.")

def exitFunc():
	"""Exit Program"""
	cls()
	exit()

def createNewAcc():
	"""Create New Account"""
	Display.displayTitle(createNewAcc.__doc__)
	serName = str(input("\nService Name: "))
	keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
	useName = str(input("User Name: "))
	keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
	pasWord = str(input("Password: "))
	keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
	grpItem = str(input("Group Item: "))
	keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
	if serName and useName and pasWord and grpItem:
		Display.createNewDply(serName,useName,pasWord,grpItem)
		while True:
			try:
				selection = str(input("\nDo you wish to continue?\nPress [Y] to save the entry into the database and [N] to discard entry: ").lower())
				keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
				if selection == "y":
					hashKey,password = enc(pasWord)
					database.insert(serName,useName,password,hashKey,grpItem)
					del pasWord #--------------> Removes the refernce object from the script
					del hashKey #--------------> Removes the refernce object from the script
					del password #--------------> Removes the refernce object from the script
					print("[MESSAGE] Account Created.")
					break
				elif selection == "n":
					cls()
					print("[MESSAGE] Account Cancelled.")
					break
				else:
					print("[ERROR] Incorrect selection. Please select [Y]es or [N]o.")
					continue
			except EOFError:
				cls()
				print("[ERROR] Invalid Entry.")
				break
	else:
		cls()
		print("[ERROR] Missing data. Please fill all detials required.")

def displayAcc():
	"""View Accounts"""
	query = database.view()
	if not query:
		print("\n[MESSAGE] No accounts in the database.")
	else:
		Display.displayAccounts()
		for entry in query:
			print("| {0:<19}|{1:^10}| {2:<39}| {3:<19}| {4:<29}|".format(entry.serviceName,entry.id,entry.userName,entry.groupItem,str(entry.dtg)))
		print("+{0:-^20}+{1:-^10}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
		while True:
			option = str(input("\nDo you wish to view more details on an account?\nPress [Y] to continue or [N] to go back to main menu: ").lower())
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			if option == "y":
				selection = str(input("\nEnter the Account Serial to view more detials: "))
				cls()
				Display.displayTitle("Account Details")
				denc(selection)
				keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
				break
			elif option == "n":
				cls()
				break
			else:
				print("[ERROR] Incorrect selection. Please select [Y]es or [N]o.")
				continue

def updateKey():
	"""Update Key"""
	query = database.view()
	Display.displayAccounts()
	for entry in query:
		print("| {0:<19}|{1:^10}| {2:<39}| {3:<19}| {4:<29}|".format(entry.serviceName,entry.id,entry.userName,entry.groupItem,str(entry.dtg)))
	print("+{0:-^20}+{1:-^10}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
	while True:
		option = str(input("\nDo you wish to edit an account.\nPress [Y] to continue or [N] to go back to main menu: ").lower())
		keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
		if option == "y":
			Id = str(input("\nEnter the Account Serial to view more detials: "))
			cls()
			Display.displayTitle("Edit Account")
			query = database.select(Id)
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			for entry in query:
				hashKeyParam = re.split("[, $]", entry.hashKey)
				print("\nSerial: ",entry.id)
				print("Service Name: ",entry.serviceName)
				print("User Name: ",entry.userName)
				print("Group Item: ",entry.groupItem)
				print("Password: ",str(entry.password)[2:-1])
				print("Hashkey: ",hashKeyParam[6]+hashKeyParam[7])
				print("Date Time Group: ",str(entry.dtg))
			pasEncrypt = str(input("\nEnter the secret word to update the password: "))
			if pasEncrypt:
				result = argon2.verify(pasEncrypt,entry.hashKey)
				keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
				if result == True:
					print("[MESSAGE] Password verified.")
					pasWord = str(input("\nEnter the new password for the account: "))
					hashKey,password = enc(pasWord)
					database.update(hashKey,password,Id)
					del pasWord #--------------> Removes the refernce object from the script
					del hashKey #--------------> Removes the refernce object from the script
					del password #--------------> Removes the refernce object from the script
					print("[MESSAGE] Account Updated.")
					keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
				elif result == False:
					cls()
					print("[ERROR] Incorrect Password. Please try again.")
				break
			else:
				cls()
				print("[ERROR] Invalid Entry.")
				break
		elif option == "n":
			cls()
			break
		else:
			print("[ERROR] Incorrect selection. Please select [Y]es or [N]o.")
			continue

def deleteAcc():
	"""Delete Account"""
	query = database.view()
	Display.displayAccounts()
	for entry in query:
		print("| {0:<19}|{1:^10}| {2:<39}| {3:<19}| {4:<29}|".format(entry.serviceName,entry.id,entry.userName,entry.groupItem,str(entry.dtg)))
	print("+{0:-^20}+{1:-^10}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
	while True:
		option = str(input("\nDo you wish to delete an account? [Y] to continue or [N] to go back to the main menu: ").lower())
		if option == "y":
			selection = str(input("\nEnter the Account Serial to be deleted: "))
			database.delete(selection)
			cls()
			print("[MESSAGE] Account number {} deleted.".format(selection))
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			break
		elif option == "n":
			cls()
			break
		else:
			print("[ERROR] Incorrect selection. Please select [Y]es or [N]o.")
			continue

def refresh():
	"""Refresh Command Prompt"""
	os.system('CLS')

def menu_loop():
	"""Password Manager Main Menu"""
	selection = None
	while selection != 0:
		try:
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			Display.displayTitle(menu_loop.__doc__)
			for key, value in menu.items():
				print('[%s] %s' %(key,value.__doc__))
			selection = int(input('\nChoose a number from the menu: '))
			keyboard.press_and_release('alt+f7') #--------------> Clears the command line history
			if selection in menu:
				menu[selection]()
		except ValueError:
			cls()
			print("\n[Error] Invalid entry")
			continue
		except EOFError:
			cls()
			print("\n[Error] Invalid entry")
			continue

if __name__ == "__main__":
	while True:
		menu = OrderedDict([(0,exitFunc),(1,createNewAcc),(2,displayAcc),(3,updateKey),(4,deleteAcc),(5,refresh)])
		menu_loop()

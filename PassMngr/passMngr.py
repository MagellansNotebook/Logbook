from collections import OrderedDict
from config_file import database
from passlib.hash import argon2
from peewee import *
import cryptography.fernet
import datetime
import base64
import os
import re

class Display():
	"""Display output"""
	def __init__(self):
		pass
	def createNewDply(serName, useName, pasWord, grpItem):
		print("\n")
		print("+{0:-^139}+".format(""))
		print("|{0:^139}|".format("New Account"))
		print("+{0:-^16}+{1:-^40}+{2:-^40}+{3:-^40}+".format("","","",""))
		print("|{0:^16}|{1:^40}|{2:^40}|{3:^40}|".format("Service Name","User Name","Password","Group Item"))
		print("+{0:-^16}+{1:-^40}+{2:-^40}+{3:-^40}+".format("","","",""))
		print("|{0:^16}|{1:^40}|{2:^40}|{3:^40}|".format(serName, useName, pasWord, grpItem))
		print("+{0:-^16}+{1:-^40}+{2:-^40}+{3:-^40}+".format("","","",""))
	def displayAccounts():
		print("\n")
		print("+{0:-^124}+".format(""))
		print("|{0:^124}|".format("Display Accounts"))
		print("+{0:-^10}+{1:-^20}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
		print("|{0:^10}| {1:<19}| {2:<39}| {3:<19}| {4:<29}|".format("Serial","Service Name","User Name","Group Item","Date Time Group"))
		print("+{0:-^10}+{1:-^20}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
	def displayTitle(name):
		print("\n")
		print("+{0:-^30}+".format(""))
		print("|{0:^30}|".format(name))
		print("+{0:-^30}+".format(""))

def enc(pasWord):
	"""Encrypt password using a secret word"""
	while True:
		try:
			pasEncrypt = str(input("\nEnter a secret word to encrypt the password: "))
			if pasEncrypt:
				hashKey = argon2.using(rounds=100).hash(pasEncrypt)
				# key encryption process
				hashKeyParam = re.split("[, $]", hashKey)
				passValue = (pasEncrypt+hashKeyParam[6][:-6]).zfill(32)
				del pasEncrypt
				del hashKeyParam
				encodeHash = base64.urlsafe_b64encode(passValue.encode('utf-8'))
				del passValue
				encVal = cryptography.fernet.Fernet(encodeHash)
				# result of encryption
				password = encVal.encrypt(pasWord.encode('utf-8'))
				del encVal
				print("[MESSAGE] Password succesfully encrypted. Press [ENTER KEY] to continue...")
				return hashKey, password
			else:
				print("[ERROR] Please enter a password. Press [ENTER KEY] to continue...")
				continue
		except ValueError:
			print("[ERROR] The password must be less than 16 characters long. Press [ENTER KEY] to continue...")
			break
		except EOFError:
			print("[ERROR] Invalid Entry. Press [ENTER KEY] to continue...")
			break

def denc(Id):
	"""Decrypt password using secret word"""
	try:
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
			if selection == "y":
				pasEncrypt = str(input("\nEnter the secret word to decrypt the password: "))
				if pasEncrypt:
					for entry in query:
						# key encryption process
						result = argon2.verify(pasEncrypt,entry.hashKey)
						if result == True:
							hashKeyParam = re.split("[, $]", entry.hashKey)
							passValue = (pasEncrypt+hashKeyParam[6][:-6]).zfill(32)
							del hashKeyParam
							del pasEncrypt
							encodeHash = base64.urlsafe_b64encode(passValue.encode('utf-8'))
							del passValue
							encVal = cryptography.fernet.Fernet(encodeHash)
							# result of encryption
							password = encVal.decrypt(entry.password)
							del encVal
							print("\nDecrypted Password: ", str(password)[2:-1])
							del password
						elif result == False:
							print("[MESSAGE] Incorrect Password!. Press [ENTER KEY] and try again.")
					break
				else:
					print("[ERROR] Please enter a password and try again.")
					continue
			elif selection == "n":
				break
			else:
				print("[ERROR] Incorrect selection. Please select [Y] or [N]. Press [ENTER KEY] to continue...")
				continue
	except EOFError:
		print("[ERROR] Invalid Entry. Press [ENTER KEY] to continue...")
	except:
		print("[ERROR] Invalid Entry. Press [ENTER KEY] to continue...")

def exitFunc():
	"""Exit Program"""
	exit()

def createNewAcc():
	"""Create New Account"""
	Display.displayTitle(createNewAcc.__doc__)
	serName = str(input("\nService Name: "))
	useName = str(input("User Name: "))
	pasWord = str(input("Password: "))
	grpItem = str(input("Group Item: "))
	if serName and useName and pasWord and grpItem:
		Display.createNewDply(serName,useName,pasWord,grpItem)
		while True:
			try:
				selection = str(input("\nDo you wish to continue?\nPress [Y] to save the entry into the database and [N] to discard entry: ").lower())
				if selection == "y":
					hashKey,password = enc(pasWord)
					database.insert(serName,useName,password,hashKey,grpItem)
					del pasWord
					del hashKey
					del password
					print("[MESSAGE] Account Created. Press [ENTER KEY] to continue...")
					break
				elif selection == "n":
					print("[MESSAGE] Account Cancelled. Press [ENTER KEY] to continue...")
					break
				else:
					print("[ERROR] Incorrect selection. Please select [Y]es or [N]o. Press [ENTER KEY] to continue...")
					continue
			except EOFError:
				print("[ERROR] Invalid Entry. Press [ENTER KEY] to continue...")
				break
	else:
		print("[ERROR] Missing data. Please fill all detials required. Press [ENTER KEY] to continue...")

def displayAcc():
	"""View Accounts"""
	query = database.view()
	if not query:
		print("\n[MESSAGE] No accounts in the database. Press [ENTER KEY] to continue...")
	else:
		Display.displayAccounts()
		for entry in query:
			print("|{0:^10}| {1:<19}| {2:<39}| {3:<19}| {4:<29}|".format(entry.id,entry.serviceName,entry.userName,entry.groupItem,str(entry.dtg)))
		print("+{0:-^10}+{1:-^20}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
		while True:
			option = str(input("\nDo you wish to view more details on an account?\nPress [Y] to continue or [N] to go back to main menu: ").lower())
			if option == "y":
				selection = str(input("\nEnter the Account Serial to view more detials: "))
				Display.displayTitle("Account Details")
				denc(selection)
				break
			elif option == "n":
				break
			else:
				print("[ERROR] Incorrect selection. Please select [Y]es or [N]o. Press [ENTER KEY] to continue...")
				continue

def updateKey():
	"""Update Key"""
	query = database.view()
	Display.displayAccounts()
	for entry in query:
		print("|{0:^10}| {1:<19}| {2:<39}| {3:<19}| {4:<29}|".format(entry.id,entry.serviceName,entry.userName,entry.groupItem,str(entry.dtg)))
	print("+{0:-^10}+{1:-^20}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
	while True:
		option = str(input("\nDo you wish to edit an account.\nPress [Y] to continue or [N] to go back to main menu: ").lower())
		if option == "y":
			Id = str(input("\nEnter the Account Serial to view more detials: "))
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
			pasEncrypt = str(input("\nEnter the secret word to update the password: "))
			result = argon2.verify(pasEncrypt,entry.hashKey)
			if result == True:
				print("[MESSAGE] Password verified.")
				pasWord = str(input("\nEnter the new password for the account: "))
				hashKey,password = enc(pasWord)
				database.update(hashKey,password,Id)
				del pasWord
				del hashKey
				del password
				print("[MESSAGE] Account Updated. Press [ENTER KEY] to continue...")
			elif result == False:
				print("[ERROR] Incorrect Password. Please try again.")
			break
		elif option == "n":
			break
		else:
			print("[ERROR] Incorrect selection. Please select [Y]es or [N]o. Press [ENTER KEY] to continue...")
			continue

def deleteAcc():
	"""Delete Account"""
	query = database.view()
	Display.displayAccounts()
	for entry in query:
		print("|{0:^10}| {1:<19}| {2:<39}| {3:<19}| {4:<29}|".format(entry.id,entry.serviceName,entry.userName,entry.groupItem,str(entry.dtg)))
	print("+{0:-^10}+{1:-^20}+{2:-^40}+{3:-^20}+{4:-^30}+".format("","","","",""))
	while True:
		option = str(input("\nDo you wish to delete an account? [Y] to continue or [N] to go back to the main menu: ").lower())
		if option == "y":
			selection = str(input("\nEnter the Account Serial to view more detials: "))
			database.delete(selection)
			print("[MESSAGE] Account number {} deleted. Press [ENTER KEY] to continue...".format(entry.id))
			break
		elif option == "n":
			break
		else:
			print("[ERROR] Incorrect selection. Please select [Y]es or [N]o. Press [ENTER KEY] to continue...")
			continue

def refresh():
	"""Refresh Command Prompt"""
	os.system('CLS')

def menu_loop():
	"""Password Manager Main Menu"""
	selection = None
	while selection != 0:
		try:
			Display.displayTitle(menu_loop.__doc__)
			for key, value in menu.items():
				print('[%s] %s' %(key,value.__doc__))
			selection = int(input('\nChoose a number from the menu: '))
			if selection in menu:
				menu[selection]()
		except ValueError:
			print("\n[Error] Invalid entry")
			continue
		except EOFError:
			print("\n[Error] Invalid entry")
			continue

if __name__ == "__main__":
	while True:
		menu = OrderedDict([(0,exitFunc),(1,createNewAcc),(2,displayAcc),(3,updateKey),(4,deleteAcc),(5,refresh)])
		menu_loop()

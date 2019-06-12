from collections import OrderedDict
from colorama import Fore, Back, Style
from peewee import *
import sys
import os
import datetime
import textwrap

db = SqliteDatabase('logbook_test.db')

class Comment(Model):
	cmt = TextField()
	timestamp = TextField()

	class Meta:
		database = db

class Logs(Model):
	msg = TextField()
	timestamp = DateTimeField(default=datetime.datetime.now)
	condition = TextField()
	logs_comment = ForeignKeyField(Comment)

	class Meta:
		database = db

def menu_loop():
	selection = None

	while selection != 0:
		print(greeting.__doc__)
		print('[Menu]:\n')

		for key, value in menu.items():
			print('[%s] %s' %(key,value.__doc__))

		selection = int(input('\nChoose a number from the menu: '))

		cls()

		if selection in menu:
			menu[selection]()

def greeting():
	"""                     ___      _______  ________   ________   ________  ________  __    __ 
		    /  /     / __   / / ____  /  / ____  /  / ___   / / ____  / / /   / /
		   /  /     / /  / / / /   /_/  / /____/ / / /   / / / /   / / / /__/ /
		  /  /     / /  / / / /_____   / _____ /  / /   / / / /   / / / ___ / 
		 /  /___  / /__/ / / /___/ /  / /___ / / / /___/ / / /___/ / / /  / /
		/______/ /______/ /_______/  /_______/  /_______/ /_______/ /_/   /_/
	"""

	print(Style.BRIGHT+Fore.GREEN+datetime+Style.RESET_ALL,'\n')

def cls():
	os.system('CLS')

def textwrap_func(data):
	return textwrap.fill(Style.BRIGHT+data+Style.RESET_ALL,initial_indent='\t',subsequent_indent='\t',width=60)

def exit_func():
	"""Exit"""

	print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,'Program Closed...')
	exit()

	cls()

def add_entry():
	"""Add Entry"""

	from datetime import datetime

	print(greeting.__doc__)
	print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'Add Entry')
	print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL+' Press [Enter] to save data or exit the main menu.')
	print(Style.BRIGHT+Fore.RED+'[Warning]'+Style.RESET_ALL+' Do not press the up/down button. The current entry will be removed from the message log.')
	print('Enter your message:\n')

	data = sys.stdin.readline().strip()

	timestamp = datetime.now().strftime('%d %B %H%M %Y')

	while True:
		selection = int(input(Style.BRIGHT+Fore.YELLOW+'\n[Comment] '+Style.RESET_ALL+'Enter the status of the message. [1] Open, [2] Close, [3] Info, [4] Exit to main menu: '))

		try:

			if not data:

				cls()

				print(Style.BRIGHT+Fore.RED+'[Error]'+Style.RESET_ALL,' No message was entered into the database.')

				break

			else:

				if selection == 1:
					status_input = 'Open'
					
				elif selection == 2:
					status_input = 'Close'

				elif selection == 3:
					status_input = 'Info'

				no_comment = Comment.create(cmt='N/A',timestamp='N/A')
				no_comment.save()
				new_logs = Logs.create(msg=data,condition=status_input,logs_comment=no_comment)
				new_logs.save()
				

				cls()

				print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,f' Message log as of {timestamp}')

				break

		except UnboundLocalError:

			cls()

			print(Style.BRIGHT+Fore.RED+'[Error]'+Style.RESET_ALL,'UnboundLocalError occured. Exiting to main menu.')

			break

def edit_entry():
	"""Edit Entry"""

	try:

		print(greeting.__doc__)
		print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'Edit Entry')

		id_input = int(input('Enter the serial number of the message: '))

		cls()

		query_id(id_input)
		print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL+' Status: [1] Open, [2] Close, [3] Info, Press [Enter] to exit')

		update_condition = int(input('Enter the new Status of the message: '))

		if update_condition == 1:
			new_condition = 'Open'
			update_cond(new_condition,id_input)

		elif update_condition == 2:
			new_condition = 'Close'
			update_cond(new_condition,id_input)

		elif update_condition == 3:
			new_condition = 'Info'
			update_cond(new_condition,id_input)

		elif update_condition == 4:
			pass

		cls()

		print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL, f'Message serial number: {id_input} updated')

	except UnboundLocalError:

		cls()

		print(Style.BRIGHT+Fore.RED+'[Error]'+Style.RESET_ALL,'UnboundLocalError occured. Exiting to main menu.')

def update_cond(new_condition,id_input):
	"""Changes the status of the message and inserts comments"""

	from datetime import datetime

	datetime = datetime.now().strftime('%d %B %H%M %Y')

	new_condition_update = Logs.update(condition=new_condition).where(Logs.id == id_input)
	new_condition_update.execute()

	if new_condition != 'Info':
		update_comment = str(input('Comment:\n'))

		new_comment_update = Comment.update(cmt=update_comment,timestamp=datetime).where(Comment.id == id_input)
		new_comment_update.execute()

def view_all():
	"""View All"""

	query = Logs.select()

	display_entry(query)

	cls()

def query_id(id_input):
	"""Search by serial number"""

	query = Logs.select().where(Logs.id == id_input)

	display_entry(query)

def dtg_func(dtg_input):
	"""Search by date"""

	query = Logs.select().where(Logs.timestamp > datetime.datetime(dtg_input[0],dtg_input[1],dtg_input[2],dtg_input[3],dtg_input[4]))

	display_entry(query)

def status(status_input):
	"""Search for Status"""

	query = Logs.select().where(Logs.condition.contains(status_input))

	display_entry(query)

def message(message_input):
	"""Seach for Messages"""

	query = Logs.select().where(Logs.msg.contains(message_input))

	display_entry(query)

def display_entry(query):
	"""View Entry"""

	count = query.count()

	logs_count = count % 5

	if logs_count != 0:
		logs_count = count // 5
		logs_count = logs_count + 1
		
	else:
		logs_count = count // 5

	for page in range(0,logs_count):
		print(greeting.__doc__)
		print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'View Entry')

		query = query.offset(page*5).limit(5)

		while True:
			for entry in query:
				timestamp = entry.timestamp.strftime('%d %B %H%M %Y')
				timestamp = Fore.GREEN+Style.BRIGHT+timestamp+Style.RESET_ALL
				entry_id = Fore.GREEN+Style.BRIGHT+str(entry.id)+Style.RESET_ALL

				if entry.condition == 'Open':
					entry.condition = Style.BRIGHT+Fore.RED+'Open'+Style.RESET_ALL

				elif entry.condition == 'Close':
					entry.condition = Style.BRIGHT+Fore.GREEN+'Close'+Style.RESET_ALL

				elif entry.condition == 'Info':
					entry.condition = Style.BRIGHT+Fore.YELLOW+'Info'+Style.RESET_ALL

				print(f'\n[Serial Number]: {entry_id} [DateTimeGroup]: {timestamp} [Status]: {entry.condition}')
				print('[Message]:\n')
				print(textwrap_func(entry.msg))

				if entry.logs_comment.cmt != 'N/A':
					print('\n\t[Comment] DTG update: ',Style.BRIGHT+Fore.GREEN+entry.logs_comment.timestamp+Style.RESET_ALL)
					print('\t[Message]:\n')
					print('\t',textwrap_func(entry.logs_comment.cmt))

			input(Style.BRIGHT+Fore.YELLOW+'\n\n[Comment]'+Style.RESET_ALL+' Press [Enter] to continue.')

			break
	
def search_entry():
	"""Search Entry"""

	print(greeting.__doc__)
	print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'Search Entry')
	print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL+' Search Parameters: [1] Serial Number, [2] DateTimeGroup, [3] Status, [4] Message Content.')

	search_value = int(input('Select the parameter number you would like to search: '))

	if search_value == 1:
		id_input = int(input('Enter the message Serial Number: '))

		cls()

		query_id(id_input)

		cls()

	elif search_value == 2:
		print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL+' DateTimeGroup')
		dtg_input = []

		year_input = int(input('Enter the message Year: '))
		if not year_input:
			dtg_input.append(2019)
		else:
			dtg_input.append(year_input)

		month_input = int(input('Enter the message Month: '))
		if not month_input:
			dtg_input.append(1)
		else:
			dtg_input.append(month_input)

		day_input = int(input('Enter the message Day: '))
		if not day_input:
			dtg_input.append(1)
		else:
			dtg_input.append(day_input)

		hour_input = str(input('Enter the message Hour:Min: '))
		if not hour_input:
			dtg_input.append(1)
		else:
			dtg_input.append(int(hour_input[0:2]))
			dtg_input.append(int(hour_input[2:4]))

		cls()

		dtg_func(dtg_input)

		cls()

	elif search_value == 3:
		print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL+' Status')
		status_input = str(input('Enter the message Status: '))
		
		cls()

		status(status_input)

		cls()

	elif search_value == 4:
		print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL+' Message Content')
		message_input = str(input('Enter the keywords you wish to search: '))

		cls()

		message(message_input)	

		cls()	

	else:

		cls()

def delete_entry():
	"""Delete Entry"""

	print(greeting.__doc__)
	print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'Delete Entry')

	delete_input = int(input('Enter the message serial number to be deleted: '))
	print(Fore.RED+Style.BRIGHT+'[Warning]'+Style.RESET_ALL,f'Message {delete_input} will be deleted.')

	if str(input('Do you wish to continue [y/n]: ')) == 'y':
		delete_message = Logs.get(Logs.id == delete_input)
		delete_message.delete_instance()

		cls()

		print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,f'Message serial number {delete_input} deleted.')

	else:

		cls()

		print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,f'Message serial number {delete_input} was not deleted.')

def save_entry():
	"""Save Logs to Text File"""

	from datetime import datetime

	datetime = datetime.now().strftime('%d-%m-%H%M-%Y')

	print(greeting.__doc__)
	print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'Save File')
	print(Style.BRIGHT+Fore.YELLOW+'[Comment]'+Style.RESET_ALL,f'All records in the database will be saved in '+datetime+'.txt')

	save_input = input('Do you wish to continue [y/n]: ')
	
	if save_input == 'y':
		with open(datetime+'.txt','w') as write_file:
			query = Logs.select()

			for entry in query:
				timestamp = entry.timestamp.strftime('%d %B %H%M %Y')
				write_file.write('[Serial Number]: '+str(entry.id)+' [DateTimeGroup]: '+timestamp+' [Status]: '+entry.condition+'\n')
				write_file.write('[Message]\n\n')
				entry_msg = textwrap.fill(entry.msg,initial_indent='\t',subsequent_indent='\t',width=60)
				write_file.write(entry_msg+'\n\n')
				
				if entry.logs_comment.cmt != 'N/A':
					write_file.write('\t[Comment] DTG update: '+entry.logs_comment.timestamp+'\n')
					write_file.write('\t[Message]\n\n')
					entry_cmt = textwrap.fill(entry.logs_comment.cmt,initial_indent='\t',subsequent_indent='\t',width=60)
					write_file.write('\t'+entry_cmt+'\n\n')

			write_file.close()

			cls()

			print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,f'Message saved as '+str(datetime)+'.txt')

	else:

		cls ()

		print(Style.BRIGHT+Fore.RED+'[Error]'+Style.RESET_ALL,'No message saved...')

def z_all():
	"""Z All"""

	print(greeting.__doc__)
	print(Style.BRIGHT+'[Menu]'+Style.RESET_ALL,'Erase All')

	z_input = input(Fore.RED+Style.BRIGHT+'[Warning]'+Style.RESET_ALL+' All files will be deleted. Do you wish to continue [y/n]: ').lower()

	if z_input == 'y':
		Logs.delete().execute()
	
		cls()

		print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,'All files deleted.')

	else:

		cls()

		print(Style.BRIGHT+Fore.CYAN+'[System]'+Style.RESET_ALL,'No message deleted')

if __name__ == "__main__":
	
	while True:

		try:
			menu = OrderedDict([(0,exit_func),(1,add_entry),(2,edit_entry),(3,view_all),(4,search_entry),(5,delete_entry),(6,save_entry),(9,z_all)])
			Logs.create_table()
			Comment.create_table()
			menu_loop()

		except KeyboardInterrupt:
			print(Style.BRIGHT+Fore.CYAN+'\n[System]'+Style.RESET_ALL,' KeyboardInterrupt intercepted. Exiting the program...')
			exit()

		except ValueError:

			cls()

			print(Style.BRIGHT+Fore.RED+'\n[Error]'+Style.RESET_ALL,'A ValueError occured.')

			continue

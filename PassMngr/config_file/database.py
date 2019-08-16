from peewee import *
import datetime

db = SqliteDatabase('accounts.db')

class Accounts(Model):
	serviceName = CharField()
	userName = CharField()
	password = BlobField(unique=True)
	hashKey = CharField(unique=True)
	groupItem = CharField()
	dtg = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = db

def insert(serviceName,userName,password,hashKey,groupItem):
	"""Create new account in the database"""
	createAcc = Accounts.create(serviceName=serviceName,userName=userName,password=password,hashKey=hashKey,groupItem=groupItem)
	createAcc.save()

def view():
	"""View all accounts"""
	query = Accounts.select().order_by(Accounts.serviceName.asc())
	return query

def select(Id):
	"""View individual account"""
	query = Accounts.select().where(Accounts.id == Id)
	return query

def update(hashKey,password,Id):
	"""Update secret key"""
	dtg = datetime.datetime.now()
	updateKey = Accounts.update(password=password, hashKey=hashKey,dtg=dtg).where(Accounts.id == Id)
	updateKey.execute()

def delete(Id):
	"""Delete Account"""
	delValue = Accounts.get(Accounts.id == Id)
	delValue.delete_instance()

db.create_tables([Accounts])

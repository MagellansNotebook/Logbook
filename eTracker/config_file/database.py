from datetime import datetime
from peewee import *
import datetime
import sys
#<---------------------------------------------------------------------------| Database
db_master = SqliteDatabase('etracker_v1.db')
#<---------------------------------------------------------------------------| Database Classes
class BaseModel(Model):
	class Meta:
		database = db_master
class MasterList(BaseModel):
	timestampMaster = DateTimeField()
	itemLoc = CharField(max_length=100)
	itemTyp = CharField(max_length=100)
	itemNSN = CharField(max_length=100)
	itemMod = CharField(max_length=100)
	itemDes = CharField(max_length=100)
	itemSer = CharField(unique=True)
	itemAss = CharField(unique=True)
	itemTrk = CharField(max_length=100)
	itemQty = IntegerField()
	class Meta:
		table_name = 'master_table'
class Track(BaseModel):
	timestampTrack = DateTimeField()
	item_location = CharField()
	item_type = CharField()
	item_nsn = CharField()
	item_model = CharField()
	item_desc = CharField()
	item_serial = CharField()
	item_asset = CharField()
	item_sca = CharField()
	item_trk = CharField()
	item_quantity = IntegerField()
	class Meta:
		table_name = 'equipment_table'
class SCANumber(BaseModel):
	scaNum = CharField(max_length=100)
	scaEList = ForeignKeyField(MasterList)
	scaETrk = ForeignKeyField(Track)
	class Meta:
		table_name = 'sca_table'
#<---------------------------------------------------------------------------| Data Base Function
def addValue(loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, date):
	"""Adding new value into the database"""
	#<---------------------------------------------------------------------------| Adds <MissingData> if value is blank
	if not loc and not typ and not nsn and not mod and not des and not qty:
		loc = "<MisingData>"
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
		qty = "<MissingData>"
	elif not loc and not typ and not nsn and not mod and not des:
		loc = "<MisingData>"
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not loc and not typ and not nsn and not mod and not des:
		loc = "<MisingData>"
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not loc and not typ and not nsn and not mod:
		loc = "<MisingData>"
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
	elif not loc and not typ and not nsn:
		loc = "<MisingData>"
		typ = "<MisingData>"
		nsn = "<MissingData>"
	elif not loc and not typ:
		loc = "<MisingData>"
		typ = "<MisingData>"
	elif not loc:
		loc = "<MisingData>"
	elif not typ and not nsn and not mod and not des and not qty:
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
		qty = "<MissingData>"
	elif not typ and not nsn and not mod and not des:
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not typ and not nsn and not mod and not des:
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not typ and not nsn and not mod:
		typ = "<MisingData>"
		nsn = "<MissingData>"
		mod = "<MissingData>"
	elif not typ and not nsn:
		typ = "<MisingData>"
		nsn = "<MissingData>"
	elif not typ:
		typ = "<MisingData>"
	elif not nsn and not mod and not des and not qty:
	 	nsn = "<MissingData>"
	 	mod = "<MissingData>"
	 	des = "<MissingData>"
	 	qty = "<MissingData>"
	elif not nsn and not mod and not des:
	 	nsn = "<MissingData>"
	 	mod = "<MissingData>"
	 	des = "<MissingData>"
	elif not nsn and not mod and not des:
		nsn = "<MissingData>"
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not nsn and not mod:
		nsn = "<MissingData>"
		mod = "<MissingData>"
	elif not nsn:
		nsn = "<MissingData>"
	elif not mod and not des and not qty:
		mod = "<MissingData>"
		des = "<MissingData>"
		qty = "<MissingData>"
	elif not mod and not des:
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not mod and not des:
		mod = "<MissingData>"
		des = "<MissingData>"
	elif not mod:
		mod = "<MissingData>"
	elif not des and not qty:
		des = "<MissingData>"
		qty = "<MissingData>"
	elif not des:
		des = "<MissingData>"	
	elif not qty:
		qty = "<MissingData>"
	# Create MasterList table
	classMasterList = MasterList.create(itemLoc=loc, itemTyp=typ, itemNSN=nsn, itemMod=mod, 
		itemDes=des, itemSer=ser, itemAss=ass, itemTrk=trk, itemQty=qty, timestampMaster=date)
	classMasterList.save()
	# Create Track table
	classTrack = Track.create(item_location=loc, item_type=typ, item_nsn=nsn, item_model=mod, 
		item_desc=des, item_serial=ser, item_asset=ass, item_sca=sca, item_trk=trk, item_quantity=qty, timestampTrack=date)
	classTrack.save()
	# Create SCANumber table
	classSCANumber = SCANumber.create(scaNum=sca, scaEList=classMasterList, scaETrk=classTrack)
	classSCANumber.save()
def delete(ser):
	"""Delete Value in the Database"""
	query =  SCANumber.select().join(MasterList).where(MasterList.itemSer == ser)
	for entry in query:
		scaId = entry.id
	# Deletes value in the MasterList Database
	deleteMaster = MasterList.get(MasterList.itemSer == ser)
	deleteMaster.delete_instance()
	# Deletes value in the Track Database
	deleteTrack = Track.get(Track.item_serial == ser)
	deleteTrack.delete_instance()
	# Deletes value in the SCA Database
	deleteSCA = SCANumber.get(SCANumber.id == scaId)
	deleteSCA.delete_instance()
def trackRec(loc, typ, nsn, mod, des, ser, ass, sca, trk,  qty, dte):
	"""Displays Track Database"""
	count = Track.select().where(Track.item_serial == ser).count()
	query = Track.select().where(Track.item_serial == ser).order_by(Track.timestampTrack.asc())
	# Keeps only 10 recorded value of the same serial number
	removeID = []
	for entry in query:
		removeID.append(entry.id)
	if count < 10:
		classTrack = Track.create(item_location=loc, item_type=typ, item_nsn=nsn, item_model=mod, 
			item_desc=des, item_serial=ser, item_asset=ass, item_sca=sca, item_trk=trk, item_quantity=qty, timestampTrack=dte)
		classTrack.save()
	else:
		# Removes the first entry
		deleteTrack = Track.get(Track.id == removeID[0])
		deleteTrack.delete_instance()
def scan(scanValue):
	"""Update Scan with a new datestamp"""
	# Current date and time
	dte = datetime.datetime.now()
	# Updates the dte in the MasterList Database
	updateScan = MasterList.update(timestampMaster=dte).where((MasterList.itemSer == scanValue) | (MasterList.itemAss == scanValue))
	updateScan.execute()
	# creates a new entry in the Track Database
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == scanValue) | (MasterList.itemAss == scanValue))
	for entry in query:
		loc = entry.scaEList.itemLoc
		typ = entry.scaEList.itemTyp
		nsn = entry.scaEList.itemNSN
		mod = entry.scaEList.itemMod
		des = entry.scaEList.itemDes
		ser = entry.scaEList.itemSer
		ass = entry.scaEList.itemAss
		trk = entry.scaEList.itemTrk
		sca = entry.scaNum
		qty = entry.scaEList.itemQty
		dte = entry.scaEList.timestampMaster
	trackRec(loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, dte)
	return query
def update(ID, loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, date):
	"""Updates any changes made in the Entries"""
	# Current date and time
	if not date:
		dateEntry = datetime.datetime.now()
	else:
		dateEntry = date
	# Updates the MasterList Database
	updateItem = MasterList.update(itemLoc=loc, itemTyp=typ, itemNSN=nsn, itemMod=mod, itemDes=des, 
		itemSer=ser, itemAss=ass, itemTrk=trk, itemQty=qty, timestampMaster=dateEntry).where(MasterList.id == ID)
	updateItem.execute()
	# Updates the MasterList Database
	updateSCA = SCANumber.update(scaNum=sca).where(SCANumber.id == ID)
	updateSCA.execute()
def fileUpload(loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, dte):
	"""Updates the MasterList if equipment exists else creates a new entry"""
	try:
		# Verifies the date column in the spreadsheet is formatted as date 
		dateCheck = datetime.datetime.strptime(dte, '%d-%b-%y')
		errorMsg = "Error"
		return errorMsg
	except TypeError:
		# Searches for the item Serial/Asset number if it exists in the database
		query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) | (MasterList.itemAss == ass))
		# Updates the MasterList Database
		if query:
			for entry in query:
				ID = entry.id
			# Updates the database entry
			update(ID, loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, dte)
			trackRec(loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, dte)
		else:
			# Creates a new database entry
			addValue(loc, typ, nsn, mod, des, ser, ass, sca, trk, qty, dte)
def viewAll():
	"""Displays All Value in Database"""
	query = SCANumber.select()
	return query
def searchSCANum():
	"""Displays all unique SCA numbers"""
	query = SCANumber.select(SCANumber.scaNum).distinct().order_by(SCANumber.scaNum.asc())
	return query
def currentDate(sca):
	currentDate = SCANumber.select().join(MasterList).where(SCANumber.scaNum == sca).order_by(SCANumber.scaNum.asc()).limit(1)
	for entry in currentDate:
		query = entry.scaEList.timestampMaster.strftime('%d-%b-%y')
	return query
#<---------------------------------------------------------------------------| Count Queries
def count():
	query = MasterList.select().count()
	return query
def countBetweenDates():
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	query = MasterList.select().where(MasterList.timestampMaster.between(dte, datetime.datetime.now())).count()
	return query
def countSerialTrack():
	query = MasterList.select().where(MasterList.itemTrk.contains("Serial Track")).count()
	return query
def countQtyTrack():
	query = MasterList.select().where(MasterList.itemTrk.contains("Qty Track")).count()
	return query
def countBetSer():
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	query = SCANumber.select().join(MasterList).where((MasterList.itemTrk.contains("Serial Track")) & 
		(MasterList.timestampMaster.between(dte, datetime.datetime.now()))).count()
	return query
def countBetQty():
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	query = SCANumber.select().join(MasterList).where((MasterList.itemTrk.contains("Qty Track")) & 
		(MasterList.timestampMaster.between(dte, datetime.datetime.now()))).count()
	return query
def countTotalUncheck():
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	check = MasterList.select().count()
	unCheck = SCANumber.select().join(MasterList).where(MasterList.timestampMaster.between(dte, datetime.datetime.now())).count()
	query = check - unCheck
	return query
def countTotalSerUncheck():
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	check =MasterList.select().where(MasterList.itemTrk.contains("Serial Track")).count()
	unCheck = SCANumber.select().join(MasterList).where((MasterList.itemTrk.contains("Serial Track")) & 
		(MasterList.timestampMaster.between(dte, datetime.datetime.now()))).count()
	query = check - unCheck
	return query
def countTotalAssUncheck():
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	check =MasterList.select().where(MasterList.itemTrk.contains("Qty Track")).count()
	unCheck = SCANumber.select().join(MasterList).where((MasterList.itemTrk.contains("Qty Track")) & 
		(MasterList.timestampMaster.between(dte, datetime.datetime.now()))).count()
	query = check - unCheck
	return query
def countSCA(sca):
	query = SCANumber.select().where(SCANumber.scaNum == sca).count()
	return query
def countBetSCASer(sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemTrk.contains("Serial Track")) & (SCANumber.scaNum == sca)).count()
	return query
def countBetSCAQty(sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemTrk.contains("Qty Track")) & (SCANumber.scaNum == sca)).count()
	return query
def countBetSCA(sca):
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	query = SCANumber.select().join(MasterList).where((MasterList.timestampMaster.between(dte, datetime.datetime.now())) & 
		(SCANumber.scaNum == sca)).count()
	return query
def countUncheck(sca):
	dte = datetime.datetime.now() - datetime.timedelta(days=30)
	check = SCANumber.select().join(MasterList).where(SCANumber.scaNum == sca).count()
	unCheck = SCANumber.select().join(MasterList).where((MasterList.timestampMaster.between(dte, datetime.datetime.now())) & 
		(SCANumber.scaNum == sca)).count()
	query = check - unCheck
	return query
#<---------------------------------------------------------------------------| NSN Queries
def displayNSN():
	query = MasterList.select(MasterList.itemNSN, MasterList.itemTyp, MasterList.itemDes).distinct().order_by(MasterList.itemDes.asc())
	return query
#<---------------------------------------------------------------------------| Search Queries
def searchID(idValue):
	query = SCANumber.select().join(MasterList).where(MasterList.id == idValue)
	return query
def searchTrackDes(serial):
	query = Track.select().where(Track.item_serial.contains(serial))
	return query
# Location
def searchLoc(loc):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc))
	return query
def searchLT(loc, typ):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ))
	return query
def searchLN(loc, nsn):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & (MasterList.itemNSN == nsn))
	return query
def searchLM(loc, mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemMod.contains(mod))
	return query
def searchLD(loc, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemDes.contains(des))
	return query
def searchLS(loc, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & (MasterList.itemSer == ser))
	return query
def searchLA(loc, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & (MasterList.itemAss == ass))
	return query
def searchLSc(loc, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & (SCANumber.scaNum == sca))
	return query
def searchLTr(loc, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTrk.contains(trk))
	return query
def searchLDt(loc, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & (MasterList.timestampMaster > date))
	return query
def searchLTN(loc, typ, nsn):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn))
	return query
def searchLTM(loc, typ, mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		MasterList.itemMod.contains(mod))
	return query
def searchLTD(loc, typ, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		MasterList.itemDes.contains(des))
	return query
def searchLTS(loc, typ, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemSer == ser))
	return query
def searchLTA(loc, typ, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemAss == ass))
	return query
def searchLTSc(loc, typ, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(SCANumber.scaNum == sca))
	return query
def searchLTTr(loc, typ, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchLTDt(loc, typ, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.timestampMaster > date))
	return query
def searchLTNM(loc, typ, nsn, mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod))
	return query
def searchLTND(loc, typ, nsn, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemDes.contains(des))
	return query
def searchLTNS(loc, typ, nsn, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & (MasterList.itemSer == ser))
	return query
def searchLTNA(loc, typ, nsn, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & (MasterList.itemAss == ass))
	return query
def searchLTNSc(loc, typ, nsn, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & (SCANumber.scaNum == sca))
	return query
def searchLTNTr(loc, typ, nsn, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemTrk.contains(trk))
	return query
def searchLTNDt(loc, typ, nsn, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & (MasterList.timestampMaster > date))
	return query
def searchLTNMD(loc, typ, nsn, mod, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des))
	return query
def searchLTNMS(loc, typ, nsn, mod, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & (MasterList.itemSer == ser))
	return query
def searchLTNMA(loc, typ, nsn, mod, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & (MasterList.itemAss == ass))
	return query
def searchLTNMSc(loc, typ, nsn, mod, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & (SCANumber.scaNum == sca))
	return query
def searchLTNMTr(loc, typ, nsn, mod, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemTrk.contains(trk))
	return query
def searchLTNMDt(loc, typ, nsn, mod, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & (MasterList.timestampMaster > date))
	return query
def searchLTNMDS(loc, typ, nsn, mod, des, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser))
	return query
def searchLTNMDA(loc, typ, nsn, mod, des, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemAss == ass))
	return query
def searchLTNMDSc(loc, typ, nsn, mod, des, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(SCANumber.scaNum == sca))
	return query
def searchLTNMDTr(loc, typ, nsn, mod, des, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchLTNMDDt(loc, typ, nsn, mod, des, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.timestampMaster > date))
	return query
def searchLTNMDSA(loc, typ, nsn, mod, des, ser, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass))
	return query
def searchLTNMDSSc(loc, typ, nsn, mod, des, ser, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (SCANumber.scaNum == sca))
	return query
def searchLTNMDSTr(loc, typ, nsn, mod, des, ser, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & MasterList.itemTrk.contains(trk))
	return query
def searchLTNMDSDt(loc, typ, nsn, mod, des, ser, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.timestampMaster > date))
	return query
def searchLTNMDSASc(loc, typ, nsn, mod, des, ser, ass, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca))
	return query
def searchLTNMDSATr(loc, typ, nsn, mod, des, ser, ass, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & MasterList.itemTrk.contains(trk))
	return query
def searchLTNMDSADt(loc, typ, nsn, mod, des, ser, ass, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (MasterList.timestampMaster > date))
	return query
def searchLTNMDSAScTr(loc, typ, nsn, mod, des, ser, ass, sca, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchLTNMDSAScDt(loc, typ, nsn, mod, des, ser, ass, sca, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchLTNMDSAScTrDt(loc, typ, nsn, mod, des, ser, ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemLoc.contains(loc) & MasterList.itemTyp.contains(typ) & 
		(MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk) & 
		(MasterList.timestampMaster > date))
	return query
# Type
def searchTyp(typ):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ))
	return query
def searchTM(typ, mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & MasterList.itemMod.contains(mod))
	return query
def searchTN(typ, nsn):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn))
	return query
def searchTM(typ, mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & MasterList.itemMod.contains(mod))
	return query
def searchTD(typ, des):
	query = SCANumber.select().join(MasterList).where( MasterList.itemTyp.contains(typ) & MasterList.itemDes.contains(des))
	return query
def searchTS(typ, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemSer == ser))
	return query
def searchTA(typ, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemAss == ass))
	return query
def searchTSc(typ, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (SCANumber.scaNum == sca))
	return query
def searchTTr(typ, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & MasterList.itemTrk.contains(trk))
	return query
def searchTDt(typ, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.timestampMaster > date))
	return query
def searchTNM(typ, nsn, mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod))
	return query
def searchTND(typ, nsn, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemDes.contains(des))
	return query
def searchTNS(typ, nsn, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		(MasterList.itemSer == ser))
	return query
def searchTNA(typ, nsn, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		(MasterList.itemAss == ass))
	return query
def searchTNSc(typ, nsn, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		(SCANumber.scaNum == sca))
	return query
def searchTTr(typ, nsn, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchTNDt(typ, nsn, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		(MasterList.timestampMaster > date))
	return query
def searchTNMD(typ, nsn, mod, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des))
	return query
def searchTNMS(typ, nsn, mod, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & (MasterList.itemSer == ser))
	return query
def searchTNMA(typ, nsn, mod, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & (MasterList.itemAss == ass))
	return query
def searchTNMSc(typ, nsn, mod, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & (SCANumber.scaNum == sca))
	return query
def searchTNMTr(typ, nsn, mod, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemTrk.contains(trk))
	return query
def searchTNMDt(typ, nsn, mod, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & (MasterList.timestampMaster > date))
	return query
def searchTNMDS(typ, nsn, mod, des, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser))
	return query
def searchTNMDA(typ, nsn, mod, des, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemAss == ass))
	return query
def searchTNMDSc(typ, nsn, mod, des, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (SCANumber.scaNum == sca))
	return query
def searchTNMDTr(typ, nsn, mod, des, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & MasterList.itemTrk.contains(trk))
	return query
def searchTNMDDt(typ, nsn, mod, des, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.timestampMaster > date))
	return query
def searchTNMDSA(typ, nsn, mod, des, ser, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass))
	return query
def searchTNMDSSc(typ, nsn, mod, des, ser, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (SCANumber.scaNum == sca))
	return query
def searchTNMDSTr(typ, nsn, mod, des, ser, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & MasterList.itemTrk.contains(trk))
	return query
def searchTNMDSDt(typ, nsn, mod, des, ser, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.timestampMaster > date))
	return query
def searchTNMDSASc(typ, nsn, mod, des, ser, ass, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca))
	return query
def searchTNMDSATr(typ, nsn, mod, des, ser, ass, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchTNMDSADt(typ, nsn, mod, des, ser, ass, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(MasterList.timestampMaster > date))
	return query
def searchTNMDSAScTr(typ, nsn, mod, des, ser, ass, sca, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchTNMDSAScDt(typ, nsn, mod, des, ser, ass, sca, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchTNMDSAScTrDt(typ, nsn, mod, des, ser, ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk) & (MasterList.timestampMaster > date))
	return query
# NSN
def searchNSN(nsn):
	query = SCANumber.select().join(MasterList).where(MasterList.itemNSN == nsn)
	return query
def searchNM(nsn, mod):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod))
	return query
def searchND(nsn, des):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemDes.contains(des))
	return query
def searchNS(nsn, ser):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & (MasterList.itemSer == ser))
	return query
def searchNA(nsn, ass):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & (MasterList.itemAss == ass))
	return query
def searchNSc(nsn, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTyp.contains(typ) & (MasterList.itemNSN == nsn) & 
		(SCANumber.scaNum == sca))
	return query
def searchNTr(nsn, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemTrk.contains(trk))
	return query
def searchNDt(nsn, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & (MasterList.timestampMaster > date))
	return query
def searchNMD(nsn, mod, des):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des))
	return query
def searchNMS(nsn, mod, ser):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		(MasterList.itemSer == ser))
	return query
def searchNMA(nsn, mod, ass):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		(MasterList.itemAss == ass))
	return query
def searchNMSc(nsn, mod, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		(SCANumber.scaNum == sca))
	return query
def searchNMTr(nsn, mod, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchNMDt(nsn, mod, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		(MasterList.timestampMaster > date))
	return query
def searchNMDS(nsn, mod, des, ser):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser))
	return query
def searchNMDA(nsn, mod, des, ass):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemAss == ass))
	return query
def searchNMDSc(nsn, mod, des, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (SCANumber.scaNum == sca))
	return query
def searchNMDTr(nsn, mod, des, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & MasterList.itemTrk.contains(trk))
	return query
def searchNMDDt(nsn, mod, des, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.timestampMaster > date))
	return query
def searchNMDSA(nsn, mod, des, ser, ass):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass))
	return query
def searchNMDSSc(nsn, mod, des, ser, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (SCANumber.scaNum == sca))
	return query
def searchNMDSTr(nsn, mod, des, ser, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & MasterList.itemTrk.contains(trk))
	return query
def searchNMDSDt(nsn, mod, des, ser, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.timestampMaster > date))
	return query
def searchNMDSASc(nsn, mod, des, ser, ass, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca))
	return query
def searchNMDSATr(nsn, mod, des, ser, ass, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchNMDSADt(nsn, mod, des, ser, ass, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (MasterList.timestampMaster > date))
	return query
def searchNMDSAScTr(nsn, mod, des, ser, ass, sca, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchNMDSAScDt(nsn, mod, des, ser, ass, sca, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & 
		(MasterList.timestampMaster > date))
	return query
def searchNMDSAScTrDt(nsn, mod, des, ser, ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemNSN == nsn) & MasterList.itemMod.contains(mod) & 
		MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & 
		MasterList.itemTrk.contains(trk) & (MasterList.timestampMaster > date))
	return query
# Model
def searchMod(mod):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod == mod)
	return query
def searchMD(mod, des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des))
	return query
def searchMS(mod, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & (MasterList.itemSer == ser))
	return query
def searchMA(mod, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & (MasterList.itemAss == ass))
	return query
def searchMSc(mod, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & (SCANumber.scaNum == sca))
	return query
def searchMTr(mod, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemTrk.contains(trk))
	return query
def searchMDt(mod, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & (MasterList.timestampMaster > date))
	return query
def searchMDS(mod, des, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser))
	return query
def searchMDA(mod, des, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemAss == ass))
	return query
def searchMDSc(mod, des, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(SCANumber.scaNum == sca))
	return query
def searchMDTr(mod, des, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchMDDt(mod, des, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.timestampMaster > date))
	return query
def searchMDSA(mod, des, ser, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass))
	return query
def searchMDSSc(mod, des, ser, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (SCANumber.scaNum == sca))
	return query
def searchMDSTr(mod, des, ser, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & MasterList.itemTrk.contains(trk))
	return query
def searchMDSDt(mod, des, ser, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.timestampMaster > date))
	return query
def searchMDSASc(mod, des, ser, ass, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca))
	return query
def searchMDSATr(mod, des, ser, ass, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & MasterList.itemTrk.contains(trk))
	return query
def searchMDSADt(mod, des, ser, ass, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (MasterList.timestampMaster > date))
	return query
def searchMDSAScTr(mod, des, ser, ass, sca, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchMDSAScDt(mod, des, ser, ass, sca, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchMDSAScTrDt(mod, des, ser, ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemMod.contains(mod) & MasterList.itemDes.contains(des) & 
		(MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk) & 
		(MasterList.timestampMaster > date))
	return query
# Description
def searchDes(des):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des))
	return query
def searchDS(des, ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser))
	return query
def searchDA(des, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemAss == ass))
	return query
def searchDSc(des, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (SCANumber.scaNum == sca))
	return query
def searchDTr(des, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & MasterList.itemTrk.contains(trk))
	return query
def searchDDt(des, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.timestampMaster > date))
	return query
def searchDSA(des, ser, ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass))
	return query
def searchDSSc(des, ser, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(SCANumber.scaNum == sca))
	return query
def searchDSTr(des, ser, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchDSDt(des, ser, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.timestampMaster > date))
	return query
def searchDSASc(des, ser, ass, sca):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass) & (SCANumber.scaNum == sca))
	return query
def searchDSATr(des, ser, ass, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass) & MasterList.itemTrk.contains(trk))
	return query
def searchDSADt(des, ser, ass, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass) & (MasterList.timestampMaster > date))
	return query
def searchDSAScTr(des, ser, ass, sca, trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchDSAScDt(des, ser, ass, sca, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchDSAScTrDt(des, ser, ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemDes.contains(des) & (MasterList.itemSer == ser) & 
		(MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk) & (MasterList.timestampMaster > date))
	return query
# Serial Number
def searchSer(ser):
	query = SCANumber.select().join(MasterList).where(MasterList.itemSer == ser)
	return query
def searchSA(ser, ass):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass))
	return query
def searchSSc(ser, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (SCANumber.scaNum == sca))
	return query
def searchSTr(ser, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & MasterList.itemTrk.contains(trk))
	return query
def searchDSDt(ser, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.timestampMaster > date))
	return query
def searchSASc(ser, ass, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca))
	return query
def searchSATr(ser, ass, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		MasterList.itemTrk.contains(trk))
	return query
def searchSADt(ser, ass, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass) & (MasterList.timestampMaster > date))
	return query
def searchSAScTr(ser, ass, sca, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchSAScDt(ser, ass, sca, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchSAScTrDt(ser, ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemSer == ser) & (MasterList.itemAss == ass) & 
		(SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk) & (MasterList.timestampMaster > date))
	return query
# Asset Number
def searchAss(ass):
	query = SCANumber.select().join(MasterList).where(MasterList.itemAss == ass)
	return query
def searchASc(ass, sca):
	query = SCANumber.select().join(MasterList).where((MasterList.itemAss == ass) & (SCANumber.scaNum == sca))
	return query
def searchATr(ass, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemAss == ass) & MasterList.itemTrk.contains(trk))
	return query
def searchADt(ass, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemAss == ass) & (MasterList.timestampMaster > date))
	return query
def searchAScTr(ass, sca, trk):
	query = SCANumber.select().join(MasterList).where((MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchAScDt(ass, sca, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchAScTrDt(ass, sca, trk, date):
	query = SCANumber.select().join(MasterList).where((MasterList.itemAss == ass) & (SCANumber.scaNum == sca) & 
		MasterList.itemTrk.contains(trk) & (MasterList.timestampMaster > date))
	return query 
# SCA
def searchSCA(sca):
	query = SCANumber.select().where(SCANumber.scaNum == sca)
	return query
def searchScTr(sca, trk):
	query = SCANumber.select().join(MasterList).where((SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk))
	return query
def searchScDt(sca, date):
	query = SCANumber.select().join(MasterList).where((SCANumber.scaNum == sca) & (MasterList.timestampMaster > date))
	return query
def searchScTrDt(sca, trk, date):
	query = SCANumber.select().join(MasterList).where((SCANumber.scaNum == sca) & MasterList.itemTrk.contains(trk) & 
		(MasterList.timestampMaster > date))
	return query
# Tracking Type
def searchTrk(trk):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTrk.contains(trk))
	return query
def searchTrDt(trk, date):
	query = SCANumber.select().join(MasterList).where(MasterList.itemTrk.contains(trk) & (MasterList.timestampMaster > date))
	return query
# Date
def searchDte(date):
	query = SCANumber.select().join(MasterList).where(MasterList.timestampMaster > date)
	return query
#<---------------------------------------------------------------------------| Initiates all Database
db_master.create_tables([MasterList,SCANumber,Track])

import uuid
import os
import json
import base64
import random
class EnigmaFortDBSafebox:
	def __init__(self, source):
		self.source = source
		self.mJs9k2mKwnx92lwmLLll = {}
	def set(self, item, value):
		self.mJs9k2mKwnx92lwmLLll[item] = self.source.encrypt(value)
	def get(self, item):
		return self.source.decrypt(self.mJs9k2mKwnx92lwmLLll[item])
	def delete(self, item):
		del self.mJs9k2mKwnx92lwmLLll[item]
	def download(self):
		return base64.b64encode(json.dumps(self.mJs9k2mKwnx92lwmLLll).encode()).decode()
	def upload(self, base):
		try:
			self.mJs9k2mKwnx92lwmLLll = json.loads(base64.b64decode(base.encode()).decode())
		except:
			raise RuntimeError("Save content is invalid.")
	def downloadfast(self):
		return json.dumps(self.mJs9k2mKwnx92lwmLLll)
	def uploadfast(self, base):
		try:
			self.mJs9k2mKwnx92lwmLLll = json.loads(base)
		except:
			raise RuntimeError("Save content is invalid.")
class EnigmaFortDBPassbox:
	def __init__(self, source, key):
		self.mw9x82958184729sjwpdmz9s82ofm = {"nothinghere": {"91949284019491840383742294029294": {"028492849102739293": base64.b64encode(str(key).encode()).decode(), "83748283843828": None, "81492739374": None}, "8374926383748": None, "8274847": None}, "83748273847": None}
		self.source = source
class EnigmaFortDB: # Recommended Secure Database
	def __init__(self, key):
		chars = 0
		chars738 = ""
		for h in key:
			if h in chars738:
				pass
			else:
				chars += 1
				chars738 += h
		del chars738
		if chars < 6:
			raise RuntimeError("We do not accept weak passwords! Error: use different characters in your password. (use 6 or more than 6 different character)")
			del self
		elif len(key) >= 16:
			key = str(key)
			newkey = "1"
			for h in key:
				newkey += str((ord(h)+9+(len(newkey)**2)+len(key)))
			newkey = int(newkey)
			self.data = EnigmaFortDBPassbox(self, newkey)
			self.key = EnigmaFortDBSafebox(self)
		else:
			raise RuntimeError("We do not accept weak passwords! Error: Your password so short. (use 16 or long than 16)")
			del self
	def set(self, item, value):
		try:
			self.key.set(self.encrypt(item), self.encrypt(value))
		except:
			raise RuntimeError("Key is invalid or unknow error.")
	def get(self, item):
		try:
			return self.decrypt(self.key.get(self.encrypt(item)))
		except:
			return None
	def delete(self, item):
		try:
			self.key.delete(self.encrypt(item))
		except:
			raise RuntimeError("Item not found or key is invalid.")
	def encrypt(self, data):
		try:
			key = int(base64.b64decode(self.data.mw9x82958184729sjwpdmz9s82ofm["nothinghere"]["91949284019491840383742294029294"]["028492849102739293"].encode()).decode())
			data = ("+"+data)[::-1]
			newdata = ""
			n = 50
			for h in data:
				newdata += chr(((ord(h)+key)+82)%1114111)
				key += n
				n += 6
			return newdata
		except:
			return None
	def decrypt(self, data):
		try:
			key = int(base64.b64decode(self.data.mw9x82958184729sjwpdmz9s82ofm["nothinghere"]["91949284019491840383742294029294"]["028492849102739293"].encode()).decode())
			newdata = ""
			n = 50
			for h in data:
				newdata += chr(((ord(h)-key)-82)%1114111)
				key += n
				n += 6
			newdata = newdata[::-1]
			if newdata.startswith("+"):
				return newdata[1:]
			else:
				return None
		except:
			return None
	def download(self):
		try:
			return self.key.download()
		except:
			return base64.b64encode("{}".encode()).decode()
	def upload(self, database):
		self.key.upload(database)
	def downloadfast(self):
		try:
			return self.key.downloadfast()
		except:
			return base64.b64encode("{}".encode()).decode()
	def uploadfast(self, database):
		self.key.uploadfast(database)
class AIDMS_Account: # Main Module
	def __init__(self, identity):
		if "a="+str(identity) in os.listdir():
			with open("a="+str(identity), "r") as f:
				db = EnigmaFortDB(str(identity)+"1234567890")
				db.uploadfast(f.read())
				self.db = db
		else:
			identity = uuid.uuid4()
			db = EnigmaFortDB(str(identity)+"1234567890")
			db.set("username", "new_"+str(random.randint(100000, 999999)))
			self.db = db
			with open("a="+str(identity), "w") as f:
				f.write(db.downloadfast())
		self.identity = str(identity)
	def set_data(self, item, value):
		self.db.set(item, value)
	def get_data(self, item):
		return self.db.get(item)
	def delete_data(self, item):
		self.db.delete(item)
	def save(self):
		with open("a="+self.identity, "w") as f:
			f.write(self.db.downloadfast())
	def load(self):
		with open("a="+self.identity, "r") as f:
			db = EnigmaFortDB(self.identity+"1234567890")
			db.uploadfast(f.read())
			self.db = db

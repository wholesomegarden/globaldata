#new.py

import time
import pickle as pk
import glob
from threading import Thread
import os.path as PATH
import os

class SelfNamed(object):
	"""docstring for SelfNamed."""
	__id = "xxx"
	def __init__(self, id = None):
		super().__init__()
		print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
		self.__id = id
		# self.arg = arg

	def __setattr__(self, name, value):
		print("EEEEEEEEEEEEEEEEEEEE---1")


	def __assign__(self, v):
		print('called with %s' % v)





class Expando(SelfNamed):
	"""docstring for Expando."""

	__id = "xxx"
	# def __init__(self, val, id = None):
	# 	super().__init__(id = id)
	# 	self.__id = id


# 	def __init__(self, val = "__17__", id = None, **entries):#, wrapper = False, main = True):
# # #expando.py
# # 		# def __init__(self):
# # 		# es=traceback.extract_stack()
# # 		super().__init__(id = id)
# # 		self.name = self.GetName()
# # 		self.__dict__.update(entries)
# # 		self.__validID_ = False
# # 		# global GD
# # 		# self.xxx = self.get_my_name()
# # 		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
# 		super().__init__(id = id)
#
# 		exist = True
# 		'''
# 		birth = str(time.time())
# 		if id is None:
# 			id = birth
# 		'''
#
# 		# self.__main__ = main
# 		self.__id__ = "hidden"
# 		self.__dict__.pop("__id__")
# 		self.val = val
# 		print("obj created! =",self.val)
# 		# self._zzz = 5
#
#
#
#
# 		# print("******---",self.get_my_name())
# 		# self["_id"] = self.get_my_name()[0]
#
# 		# self.xxx.yyy.zzz = 13
# 		# updateID = Thread(target = self.makeID, args = [list,])
# 		# updateID.start()
#
# 		print("AAAAAAAAAAA	AAA",entries,self.__name__)
# 		for arg_name in entries:
# 			print("AAAAAAAAAAAAA",arg_name)

	def __init__(self, val = None, id = None, main = True, **entries):#, wrapper = False, main = True):
	#expando.py
		# def __init__(self):
		# es=traceback.extract_stack()
		super().__init__(id = id)
		print("PPPPPPPPPPPPPP", id)
		# self.name = self.GetName()

		self.__dict__.update(entries)
		self._name = id
		self._id = id
		# self.__validID_ = False
		# global GD
		# self.xxx = self.get_my_name()
		# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
		exist = True
		'''
		birth = str(time.time())
		if id is None:
			id = birth
		'''

		# self.__main__ = main
		self.__id__ = "hidden"
		self.__dict__.pop("__id__")
		self.val = val
		print("obj created! =",self.val)
		self._zzz = 5
		# print("******---",self.get_my_name())
		# self["_id"] = self.get_my_name()[0]

		# self.xxx.yyy.zzz = 13
		# updateID = Thread(target = self.makeID, args = [list,])
		# updateID.start()

		print("AAAAAAAAAAA	AAA",entries,self.__name__)
		for arg_name in entries:
			print("AAAAAAAAAAAAA",arg_name)

	def __hash__(self):
		print(hash(str(self)))
		return hash(str(self))

	def getID(self):
		return self.__id__


	def __set__(self, key, val):
		print("eeeeeeeeeeeeeeeeeeeee")
		self.__dict__[key] = val
		return True

	def __get__(self,key):
		print("eeeeeeeeeeeeeeeeeeeeeaaa")
		return self.__dict__[key]



	def __setattr__(self, name, value):
		print("EEEEEEEEEEEEEEEEEEEE1")
		if "str" not in str(type(name)):
			name = str(name)
		if "_" not in name and "val" in self.__dict__ and name is not "val":# and "__skip" in self.__dict__ and name not in self.skip:
			if "new.obj" not in str(type(value)):
				print("_____________________",str(type(value)))
				if name not in self.__dict__:
					print("2222222222")
					self[name] = obj(id = self._id+"/"+name, val= value)
				else:
					print("33333333")
					# self.__set__(name,value)
					manager.save(channel = self._id+"/"+name, data=value)
					# self.save(id = self._id+"/"+name, val= value)
			else:
				print("44444")
				self.__dict__[name] = value

		else:
			print("555555555")
			self.__dict__[name] = value

	def __getitem__(self, name):
		if "str" not in str(type(name)):
			name = str(name)

		if "_" not in name and "val" in self.__dict__ and name is not "val" and name not in self.__dict__:
			self.__dict__[name] = obj(id = self._id+"/"+name)

		if name in self.__dict__:
			# print("FUUCKKKKKKKKKKKKKKKKKKKKKk")

			item = self.__dict__[name]
			return item

			atr = object.__getattribute__(self, name)
			return atr




	def __assign__(self, v):
		print('called with %s' % v)

	def __setitem__(self, name, value):
		print("iiiiiiiiiiiiiiiiioooooooo")
		if "str" not in str(type(name)):
			name = str(name)
		if "_" not in name and "val" in self.__dict__ and name is not "val":# and "__skip" in self.__dict__ and name not in self.skip:
			print("VVVVVVVV",str(type(value)))
			if "new.obj" not in str(type(value)):
				print("_____________________",str(type(value)))
				if name not in self.__dict__:
					print("1",name)
					self.__dict__[name] = obj(id = self._id+"/"+name, val = value)
				else:
					print("2",name)
					self[name].set(value)
			else:
				print("22222222222222222222222",name,value)
				self.__dict__[name] = value
				print("YESSSSSSSSS",	self.__dict__[name])
		else:
			print("3",name)
			self.__dict__[name] = value

		# print("FINISHED SETTING ITEM", self.__dict__)

	def __getattribute__(self, name, loop = True):
		if "str" not in str(type(name)):
			name = str(name)
		atr = object.__getattribute__(self, name)
		return atr
	def __getattr__(self, name, loop = True):
		print("getttt")
		if "str" not in str(type(name)):
			name = str(name)
		# return name
		if "_" not in name and "val" in self.__dict__ and name is not "val" and name not in self.__dict__:
			print("OOOOO_ooooooooooooooooooooo",name)#,self.__dict__)
			print("aaaaaaaaaaaaaa")
			self[name] = obj(id = self._id+"/"+name)
		if name in self.__dict__:
			print("bbbbbbbbbbbbbbb")
			atr = object.__getattribute__(self, name)

			return atr
		# return 13
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx")

	def set(self, val):
		self.val = val

	def __getstate__(self):
		print ("I'm being pickled")
		print(self.__dict__)
		print()
		return False

	def __setstate__(self, d):
		pprint ("I'm being unpickled with these values:", d)
		self.__dict__ = d
		# self.val *= 3

	def __repr__(self):
		return str({str(self._name):self.val})

		return str({"val":self.val})
		return str(self.val)+", "+str(self.__dict__)
		return str([self.val, self.__dict__])

	# def

	def __str__(self):
		return str({str(self._name):self.val})
		return str({"val":self.val})
		return str(self.val)
		return str(self.__get__())

	def __is__(self, other):
		return self.__eq__(other)

	# by value of main
	def __eq__(self, other):
		if self.__isObj(other):
			return self.val == other.val
		elif "str" in str(type(other)):
			return str(self.val) == other
		return self.val == other

	def __add__(self, other):
		# print("!!!!!!!!!")
		# print(type(other))
		# print()
		if self.__isObj(other):
			return self.val[0] + other.val[0]
		elif "str" in str(type(other)):
			return str(self.val[0]) + other
		return self.val[0] + other

	def __radd__(self,other):
		return self.__add__(other)

	def __rsub__(self,other):
		print(type(other))
		print()
		if self.__isObj(other):
			return other.val[0] - self.val[0]
		elif "str" in str(type(other)):
			print("::::::::::::::xxxx:::::::::")
			return other - str(self.val[0])
		return other - self.val[0]

	def __pos__(self, other):
		# print("!!!!!!!!!")
		# print(type(other))
		# print()
		if self.__isObj(other):
			return self.val + other.val
		elif "str" in str(type(other)):
			return str(self.val) + other
		return self.val + other

	def __sub__(self, other):
		# print("!!!!!!!!!")
		print(type(other))
		print()
		if self.__isObj(other):
			return self.val[0] - other.val[0]
		elif "str" in str(type(other)):
			print("::::::::::::::xxxx:::::::::")
			return str(self.val[0]) - other
		return self.val[0] - other

	def __neg__(self, other):
		# print("!!!!!!!!!")
		# print(type(other))
		# print()
		if self.__isObj(other):
			return self.val + other.val
		elif "str" in str(type(other)):
			return self.val + other

	def __isObj(self, o):
		# print("############################",str(type(o)))
		# time.sleep(100)
		print("@@@@@@@@@@@@@@@@@@@@@@asdasdasd")
		return "new.obj" in str(type(o))

	def __call__(self, *vars):
		print(":::::::::::::::::::::::")
		for v in vars:
			print(v)
		print(":::::::::::::::::::::::")


	def show(self,t = "    ",count = 0):
		# print("ssssssssssssssss..............")
		s = ""
		# print("///////////",self.val,type(self.val))

		if "str" in str(type(self.val)):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self.val)+s
		tab = ""
		for i in range(count):
			tab+=t

		p = tab+p
		print(p)
		for a in self.__dict__:
			if "new.obj" in str(type(self.__dict__[a])):
				self.__dict__[a].show(count= count+1)



Dir = "Y/GlobalData/"
ExtKey = ".gdc"
ExtData    = ".gdd"
wait = 0.00001
hasManager = False
channels = {}

class __objManager(object):
	"""docstring for objManager."""

	ExtKey = ""
	ExtKey = ""
	dir = ""
	channels = {}
	__id = "xxx"
	_checkCounter = 0
	_fin = False

	def __init__(self, **entries):
		global hasManager, Dir, ExtKey, ExtData, channels
		if hasManager:
			print("FFFFFFFFFFFFFFFFFF")
			return None
		self._checkCounter = 0
		self._fin = False
		print("New Manager!!")
		# super(objManager, self).__init__()
		dbexist = PATH.exists(Dir)
		if not dbexist:
			os.makedirs(Dir)

		self.__dict__.update(entries)

		self.dir = Dir
		self.ExtKey = ExtKey
		self.ExtData = ExtData
		self.channels = channels
		print("VVVVVVVVVVVVVVVVVVV")
		# self.__channelKeys = {}
		# self.__channelValues = {}
		self.refreshChannels()


	def refreshChannels(self):
		T = Thread(target=self.checkChannels, args=[self,])
		T.start()

	def checkChannels(self, data = [None,]):
		global channels, wait
		# global _checkCounter
		if self._checkCounter > 1000000:
			self._checkCounter = 1
			for i in range(100):
				print("_checkCounter == 1000000")
		# self = data[0]
		while True:

			chKeys = channels.keys()
			cKeys = []
			discovery = False
			for k in chKeys:
				cKeys.append(k)
			for channel in cKeys:
				innerDirs = glob.glob(self.dir+channel+"/*/")
				for i in innerDirs:
					d = i[len(self.dir+channel)+1:-1]
					# print("DDDDDDDDDD",d)
					if channel+"/"+d not in channels:
						self._fin = False
						discovery = True
						if channels[channel]["ref"] is not None and len(channels[channel]["ref"])>1:
							print("DUPPPPPPPPPPPPPPPPPPPPPPPPPPPp")
						elif channels[channel]["ref"] is not None and len(channels[channel]["ref"])>0:
							channels[channel]["ref"][0][0][d] = obj(id=channel+"/"+d)
						else:
							print("XRRXRXRXRXRXrXR")

				key = self.loadKey(channel)
				# print("channel",channel)
				try:

					if key > channels[channel]["key"][0]:
						print("!!!!!!! UPDATED",channel,key)
						self.setChannel(channel,key,self.loadData(channel))
					else:
						# print("passed", channel, key)
						pass
				except:
					print("XXXXXXXX",channel)

			if not discovery:
				self._fin = True


			time.sleep(wait)
			self._checkCounter += 1

	def setChannel(self, channel, key, value):
		global channels
		if channel in channels:
			channels[channel]["key"][0] = key
			channels[channel]["val"][0] = value



	def getChannel(self, channel):
		global channels
		if channel not in channels:

			channels[channel] = {"key":[-1],"val":[None], "ref":[]}
			# channelsKeys[channel] = [-1]
			# channelsBindings[channel] = value

			loaded = self.load(channel) ## TODO: Create if not exist
			self.setChannel(channel, loaded["key"],  loaded["val"])
			# channels[channel]["key"][0] = loaded["key"]
			# channels[channel]["val"][0] = loaded["val"]
		# else:
		return channels[channel]


	def zero(self,c=1):
		return 0*c

	def setChannelRef(self, channel, ref = None):
		global channels
		if channel in channels:
			if ref is not None:
				if channels[channel]["ref"] is None:
					channels[channel]["ref"] = []
				channels[channel]["ref"].append(ref)
				print("V V V V V V V V V VVVVVVVVVVVV VVVVVVVVVVV VVVVVVVVVVVVV",channel,channels[channel]["ref"] )
				# while(len(channels[channel]["ref"])>1):
				# 	first = channels[channel]["ref"][0]
				# 	print("\n\nFIRST:::",repr(first))
				# 	last = channels[channel]["ref"][-1]
				# 	print("\n\nLAST::::",repr(last))
				# 	last = first
				# 	print("\n\nLAST2::::",repr(last))

	def bind(self, channel, value = None, ref = None):
		if channel is None:
			print("!!!!!!")
			return self.zero(12)/self.zero(1)

		data = self.getChannel(channel)
		self.setChannelRef(channel, ref = ref)
		# if value is None:
		# 	value = [None]

		# else:
		# 	# prev = self.get(channel)
		# 	if value[0] is None:
		# 		prev = self.getValue(channel)
		# 		value[0] = prev[0]
		# 	else:
		# 		self.save(channel, value)

		if value is not None:
			# value[0] = self.getValue(channel)
			self.save(channel, value)

		return data["val"] # BINDED! [var]


	def loadAbs(self, filename):
		# run = True
		# untilTrue = False
		if not PATH.exists(filename):
			# print("filename",filename, "doesn't exist")
			return None

		try:
			data = None
			with open(filename,"rb") as file:
				return pk.load(file)
				#self.printF("loaded",data, "from",filename)
			return data
		except:
			pass
			# if untilTrue:
			# 	self.printF("ERR - Try again, loading",filename)
			# 	time.sleep(0.1)
			# 	self.load(filename)
		return None

	def load(self, channel):
		global manager
		self.checkDirs(channel)
		filenameData = self.dir + channel + self.ExtData
		filenameKey = self.dir + channel + self.ExtKey


		if not PATH.exists(filenameKey) or not PATH.exists(filenameData):
			data = self.loadAbs(filenameData)
			self.save(channel, data = data)

		return {"key":self.loadKey(channel),"val":self.loadData(channel)}

	def loadData(self, channel):
		filenameData = self.dir + channel + self.ExtData
		if PATH.exists(filenameData):
			return self.loadAbs(filenameData)

		return None
	#
	# def loadKey(self, channel):
	# 	filenameKey = self.dir + channel + self.ExtKey
	# 	return self.loadAbs(filenameKey)
	#


	def loadKey(self,channel):
		filenameKey = self.dir + channel + self.ExtKey
		if PATH.exists(filenameKey):
			return self.loadAbs(filenameKey)

		return None


	def checkDirs(self, channel):
		clist = channel.split("/")
		bigList = []
		for i in range(len(clist)):
			str = ""
			for c in range(i+1):
				str+=clist[c]+"/"
			bigList.append(str)
		for B in bigList:
			if not PATH.exists(self.dir+B):
				print("### CREATING DIR",self.dir+B)
				os.makedirs(self.dir+B)


	def save(self, channel, data):
		global channels

		filenameData = self.dir + channel + self.ExtData
		filenameKey = self.dir + channel + self.ExtKey

		self.checkDirs(channel)
		newKey = -1
		# if not PATH.exists(filename):

		### TODO: optional backup here before overwriting

		if PATH.exists(filenameKey):
			newKey = self.loadKey(channel)
			if newKey is None:
				newKey = -1
			newKey += 1

		print("SAVING ALL")
		self.saveAbs(filenameData, data)
		self.saveAbs(filenameKey, newKey)
		channels[channel]["key"][0] = newKey
		channels[channel]["val"][0] = data

	def saveAbs(self, filename, data):
	#    with open(filename,"wb") as file:
	#        pk.dump(data,file)
	#        self.printF("saved",data)

		# self.printF("data to be saved:",data)
		# self.printF("path:",filename)

		print("SAVING ABS",filename, data)
		try:
			# print("..........tring to save at ",filename)
			with open(filename,"wb") as file:
				# print("iiiiinnnnnnnn")
				pk.dump(data,file)
				# self.printF("saved",str(data), "@",filename)
				# run = False
			#
			return True
		except Exception as e:
			# try:
			# 	print("..........tring to save at ",filename)
			# 	with open(filename,"wb") as file:
			# 		print("iiiiinnnnnnnn")
			# 		pk.dump(str(data),file)
			# 		self.printF("saved",str(data), "@",filename)
			# 		run = False
			# 	# del(data)
			# 	### ???
			# 	# print("//////////////////////////")
			# 	return True
			# except Exception as ee:
			# 	print("XXXXXXX failed saving",str(ee))
			# 	time.sleep(0.01)
			print("XXXXXXX failed saving",str(e))
			time.sleep(0.01)


		# def ox(id = None, val = None):
		# 	global manager
		# 	print("!!!!!! oooooo", manager.channels)
		# 	if id in manager.channels:
		# 		print("iddddddddddddd",id)
		# 		if manager.channels[id]["ref"] is not None and len(manager.channels[id]["ref"])>0:
		# 			print("VVVVVVVV VVVVVVVVVV VVVVVVV V V V V V V V V V VV UUUUUUUUUU",id,"       ",manager.channels[id]["ref"][0])
		# 			if val is not None:
		# 				manager.save(channel = id, data = val)
		# 				# pass
		# 			return manager.channels[id]["ref"][0][0]
		# 		else:
		# 			print("NEW OBJ")
		# 			return obj(val = val, id = id)
		# 	else:
		# 		print("NEW OBJ")
		# 		return obj(val = val, id = id)
	def ox(self,id = None, val = None):
		return ox(id = id, val = val)


def newObjManager():
	global hasManager
	if not hasManager:

		manager = __objManager()
		hasManager = True
		return manager
	return manager

manager = newObjManager()


def HHH():
	print("HHHHHHHHHHHHHHHHHHHHH")
	print("HHHHHHHHHHHHHHHHHHHHH")
	print("HHHHHHHHHHHHHHHHHHHHH")
	print("HHHHHHHHHHHHHHHHHHHHH")
	print("HHHHHHHHHHHHHHHHHHHHH")
	print("HHHHHHHHHHHHHHHHHHHHH")


def ox(id = None, val = None):
	global manager
	print("!!!!!! oooooo", manager.channels)
	if id in manager.channels:
		print("iddddddddddddd",id)
		if manager.channels[id]["ref"] is not None and len(manager.channels[id]["ref"])>0:
			print("VVVVVVVV VVVVVVVVVV VVVVVVV V V V V V V V V V VV UUUUUUUUUU",id,"       ",manager.channels[id]["ref"][0])
			if val is not None:
				manager.save(channel = id, data = val)
				# pass
			return manager.channels[id]["ref"][0][0]
		else:
			print("NEW OBJ")
			return obj(val = val, id = id)
	else:
		print("NEW OBJ")
		return obj(val = val, id = id)
	# global manager
	# return manager.ox(id = id, val = val)

class obj(Expando):
	"""docstring for obj."""

	def __init__(self, val = None, id = None):
		global manager
		self.__id = id
		super().__init__(val = val, id = id)

		self._myManager = manager
		self.__id = id
		print("!!!!!!!!", self.__id)
		self.val = manager.bind(self.__id, val, ref = [self])

	def Show(self):
		print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().show()

	def whileShow(self):
		while(True):
			self.show()
			time.sleep(0.2)
			os.system("clear")

	def turnTo5(self):
		print("5555555555555555")
		self = 5

	def set(self, value):
		# id = self._id+"/"+name, val= value
		manager.save(self._id,value)

	def __setattr__(self, name, value):
		print("EEEEEEEEEEEEEEEEEEEE000")
		return super().__setattr__(name = name, value=value)
	def __getitem__(self, name):
		return super().__getitem__(name = name)
	def __setitem__(self, name, value):
		return super().__setitem__(name = name, value=value)
	def __getattribute__(self, name, loop = True):
		return super().__getattribute__(name = name, loop=loop)
	def __getattr__(self, name, loop = True):
		return super().__getattr__(name = name, loop=loop)


# from xo import *

# ano = newObjManager()
# ano2 = objManagenor()

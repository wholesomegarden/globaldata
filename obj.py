#expando.py

# from GlobalData.R import *
from GlobalData.GlobalData import *

from pprint import *




from pprint import *
import os, time


class ext(dict):
	def __init__(self):
		self._x = "xxxxxxxxx"

	def x(self):
		pass
		pass##print(self._x)

def updateListT(args):
	updateD, GD = args
	print ('static method calledvvvv')
	print ('static method called')
	print ('static method called')
	print ('static method called')
	print ('static method called')
	print ('static method called')
	print ('static method calledaaaaaa')
	while (True):
		# print ('static method calledxxxxxxxxx',list)
		newD = []
		dirLen = GD.dir
		try:
			for key in obj.updated:
				len
				innerDirs = glob.glob(GD.dir+key+"/*/")
				# ikeys = []
				# for i in innerDirs:
				#
				# 	ikeys.append(m)
				for i in innerDirs:
					d = i[:][len(dirLen):-1].split("/")[-1]
					# print("iiiiiiiiiiiiiiiii:::::",d)
					# print("iiiiiiiiiiiiiiiii:::::",d)
					# print("iiiiiiiiiiiiiiiii:::::",d)
					pass##print("DDDDDDDDDDDDD:::::::::::",d)
					if key+"/"+d not in obj.updated:
						print(d,"obj.updatedobj.updatedobj.updated\n",obj.updated)
						print("iiiiiiiiiiiiiiiii:::::",key+"/",d)
						newD.append([d,obj.updated[key]])
		except:
			pass
			# print(";;;",a)
		for key, o in newD:
		# 	print("KKKKKKKKKKKKKKK:", key)
		# 	print("KKKKKKKKKKKKKKO:", o._id)
			if key not in o.__dict__:
				print("keyyyyyyyyy",key)
				o[key] = GD.GetX(o._id+"/"+key)
		# 	print("KKKKKKKKKKKKKKR:", prevItem)
		# 	# updateD.append(key)
		# # 	# if key not in o.__dict__:
		# 	o[key]
			# o[key] = obj(key,val = prevItem)
			# o[key].set(prevItem)

		time.sleep(.1)

# @staticmethod
def updateList(args):
	list = args
	print ('static method calledfffffffffff')
	print ('static method called')
	print ('static method called')
	print ('static method called')
	print ('static method called')
	print ('static method called')
	print ('static method calledffffff')
	update = Thread(target = updateListT, args = [list,])
	update.start()



### NEXT: update bindings to class staticmethod

#class RememberInstanceCreationInfo:
class RICI(object):
	def GetName(self):
		for frame, line in traceback.walk_stack(None):
			varnames = frame.f_code.co_varnames
			if varnames is ():
				break
			if varnames[0] in frame.f_locals and frame.f_locals[varnames[0]] not in (self, self.__class__):
				break
				# if the frame is inside a method of this instance,
				# the first argument usually contains either the instance or
				#  its class
				# we want to find the first frame, where this is not the case
		else:
			raise InstanceCreationError("No suitable outer frame found.")
		self._outer_frame = frame
		self.creation_module = frame.f_globals["__name__"]
		self.creation_file, self.creation_line, self.creation_function, \
			self.creation_text = \
			traceback.extract_stack(frame, 1)[0]
		self.creation_name = self.creation_text.split("=")[0].strip()
		print("$$$$$$$$$$$$$$",self.creation_name)
		if len(self.creation_name) < 1:
			cmd = readline.get_history_item(readline.get_current_history_length())
			self.name = re.split('=| ',cmd)[0]
		else:
			self.name = self.creation_name


	def __init__(self):
		self.GetName()


		super().__init__()
		# threading.Thread(target=self._check_existence_after_creation).start()

	def _check_existence_after_creation(self):
		while self._outer_frame.f_lineno == self.creation_line:
			time.sleep(0.01)
		# this is executed as soon as the line number changes
		# now we can be sure the instance was actually created
		error = InstanceCreationError(
				"\nCreation name not found in creation frame.\ncreation_file: "
				"%s \ncreation_line: %s \ncreation_text: %s\ncreation_name ("
				"might be wrong): %s" % (
					self.creation_file, self.creation_line, self.creation_text,
					self.creation_name))
		nameparts = self.creation_name.split(".")
		try:
			var = self._outer_frame.f_locals[nameparts[0]]
		except KeyError:
			raise error
		finally:
			del self._outer_frame
		# make sure we have no permament inter frame reference
		# which could hinder garbage collection
		try:
			for name in nameparts[1:]: var = getattr(var, name)
		except AttributeError:
			raise error
		if var is not self: raise error

	def __repr__(self):
		return super().__repr__()[
			   :-1] + " with creation_name '%s'>" % self.creation_name

import traceback
import readline
import re

class obj(RICI):
	expand = time.time() # Make dict
	expand_gap = 0.3
	GD = GlobalData()


		# while (True):
		# 	print ('static method called',list)


	updateStarted = False
	updated = {}
	updateList([updated, GD])
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

	def getID(self):
		return self._id

	def setID(self, id):
		self.__id = id
		return self._id

	def getSelf(self):
		return self
	# def __init__(self, id = None, val = None):#, wrapper = False, main = True):

	def updateChildren(self, data):
		pass
		# GD = obj.GD
		# pass##print("Updating children of",data)
		# prevList = glob.glob(GD.dir+self._id+"/*/")
		# while(True):
		# 	time.sleep(0.3)
		# 	innerDirs = glob.glob(GD.dir+self._id+"/*/")
		# 	added, removed = self.compareLists(prevList,innerDirs)
		# 	pass##print()
		# 	pass##print(self._id, "prevList dirs:",prevList)
		# 	pass##print(self._id, "inner dirs:",innerDirs)
		# 	pass##print()
		#
		# 	for add in added:
		# 		d = add[:-1].split("/")[-1]
		# 		if d not in self.__dict__:
		# 			pass##print("Adding ",add, " binding to ",self._id)
		# 			# pass##print("DDDDDDDDDDDDD:::::::::::",d)
		# 			prevItem = GD.GetX(self._id+"/"+d)
		# 			self[d] = obj(self._id+"/"+d,val = prevItem)
		# 			pass##print("loaded ",self._id+"/"+d, "with ",prevItem)
		#
		# 	for rem in removed:
		# 		d = add[:-1].split("/")[-1]
		# 		if d in self.__dict__:
		# 			self.__dict__.pop(d)




	def __init__(self, val = "__171__", id = None, rec = True, **entries):#, wrapper = False, main = True):

		if id is None:
			super().__init__()
			print("RRRRRRRRR",self.name)
			id = self.name

		GD = obj.GD
		loaded = False

		self._id = id
		obj.updated[self._id] = self


		# if not loaded:
		# 	pass##print("NNNNNOOOOOTTTTTT LOADEDDDDDDDDD")
		if True:

			# def __init__(self):
			# self.__dict__.update(entries)

			self._entries = entries
			# global GD
			exist = True
			'''
			birth = str(time.time())
			if id is None:
				id = birth
			'''

			# self.__main__ = main
			# self["__id__"]= "hidden"
			self._binded = []
			# self["__skip__"] = ["exist","_binded","skip","gd","o","__id","pre", "main", "val","root"]


			# self.__dict__.pop("_id")
			self.val = val


			self._birth = time.time()
			if id is None:
				id = str(self._birth)


			dir = GD.dir+id+"/"
			dbexist = PATH.exists(dir)
			if not dbexist:
				os.makedirs(dir)


			# self.__bindAll__()

			# if val is not None:
			# 	GD.SaveX(id, val)
			pass##print("obj created! =",self._id," == ",self.val)


			pass##print("new Obj",self._id,"........................")
			if rec and self._id is not None:
				folderExist = PATH.exists(GD.dir+self._id)
				if folderExist:
					prevValue = GD.GetX(self._id)
					if val is "__171__":
						val = prevValue

					pass##print("PREV",prevValue)
					# o = obj(self._id = self._id, val = prevValue, rec = False)
					innerDirs = glob.glob(GD.dir+self._id+"/*/")
					pass##print("inner::::::::::",innerDirs)

					for di in innerDirs:
						d = di[:-1].split("/")[-1]
						pass##print("DDDDDDDDDDDDD:::::::::::",d)
						prevItem = GD.GetX(self._id+"/"+d)
						self[d] = obj(id = self._id+"/"+d,val = prevItem)
						pass##print("loaded ",self._id+"/"+d, "with ",prevItem)
					# self = o.getSelf()
					loaded = True
					pass##print("LLLLLLLOOOOOOOOOOOOAAAAAADDDDDDEDDDDDDDD")

				else:
					pass##print("XXXXXXXXXXXXXXXXXXXXXXx1",GD.dir+self._id)


			# GD.SaveX(self._id,val)
			self.val = GD.bind(self._id)
			self.set(val)

			# tt = Thread(target = self.updateChildren, args = [self._id,])
			# tt.start()

	def show(self,t = "    ",count = 0):
		s = ""
		if "str" in str(type(self.val[0])):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self.val[0])+s
		tab = ""
		for i in range(count):
			tab+=t

		p = tab+p
		print(p)
		for a in self.__dict__:
			if "obj.obj" in str(type(self.__dict__[a])):
				self.__dict__[a].show(count= count+1)

#
# while(True):
# 	o.show()
# 	time.sleep(0.1)
# 	os.system("clear")
#

		# for child in

	def whileShow(self):
		while(True):
			self.show()
			time.sleep(0.2)
			os.system("clear")

	def __bindAll__(self):
		# global GD
		# gd = GD
		# if gd is None:
		# 	gd = GD
		GD = objO.GD

		pre = self._id+"/"
		# pass##print("XXXXXXXXXXXXXXXXXXXXXXXX")
		# pass##print("XXXXXXXXXXXXXXXXXXXXXXXX")
		# pass##print("XXXXXXXXXXXXXXXXXXXXXXXX")
		# pass##print("XXXXXXXXXXXXXXXXXXXXXXXX")
		# pass##print("XXXXXXXXXXXXXXXXXXXXXXXX")
		# pass##print("XXXXXXXXXXXXXXXXXXXXXXXX")
		for key in list(self.__dict__):
			# if key not in self.skip:
			if not key.startswith("_"):
				pass##print("")
				pass##print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>x")
				fkey = self._id+"/"+key
				pass##print("saving key",fkey)
				val = self[key]
				res = GD.SaveX(fkey,val)
				if fkey not in self.binded:
					self.binded.append(fkey)
					if res:
						self[key] = GD.bind(fkey)
						pass##print("bindded successfully")
				pass##print()
			else:
				pass##print("IIIIIIIIIIIIgnoring ",key)

		pass##print("YYYYYYYYYYYYYYYYYYYYYYYY")
		for key in list(self.__dict__):
			# if key not in self.skip:
			if not key.startswith("_"):
				pass##print("")
				pass##print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>y")
				fkey = self.pre+key
				pass##print("binding key",fkey)
				val = self[key]
				if fkey not in self.binded:
					# res = GD.SaveX(pre+key,val)
					self.binded.append(fkey)
					# if res:
					self[key] = GD.bind(fkey)
					pass##print("bindded successfully")
				pass##print()
			else:
				pass##print("IIIIIIIIIIIIgnoring ",key)


	def __setattr__(self, name, value):
		GD = obj.GD
		time.sleep(0.01)
		if "str" not in str(type(name)):
			name = str(name)
		if not name.startswith("_") and "val" in self.__dict__ and name is not "val":# and "__skip" in self.__dict__ and name not in self.skip:
			if "obj.obj" not in str(type(value)):
				if name not in self.__dict__:
					self[name] = obj(id = self._id+"/"+name, val= value)
				else:
					self[name].set(value)

				# if name not in self._binded:
				# 	self.__dict__[name].set(GD.bind(self._id+"/"+name))
				# 	self._binded.append(name)

				# GD.SaveX(self._id+"/"+name,value)
			else:
				self.__dict__[name] = value

		else:
			self.__dict__[name] = value

	def __getitem__(self, name, rec = True):

		# if rec and name is "val":
		# 	pass##print("VVVVVVVVVVVVVVV v v v v val[0]")
		# 	return self.
		if "str" not in str(type(name)):
			name = str(name)

		print("NAME",name)
		print("NAME",name)
		print("NAME",name)
		print("NAME",name)
		print("NAME",name)
		if not name.startswith("_") and "val" in self.__dict__ and name is not "val" and name not in self.__dict__:
			self.__dict__[name] = obj(id = self._id+"/"+name)
		if name in self.__dict__:
			atr = self.__dict__[name]
			# if name is "val" and "list" in str(type(atr)) and len(atr) is 1:
			# 	return atr[0]
			if name is "val":# and "list" in str(type(atr)) and len(atr) is 1:
				return atr[0]
			return atr

			atr = object.__getattribute__(self, name)
			return atr



	def __setitem__(self, name, value):
		GD = obj.GD

		if "str" not in str(type(name)):
			name = str(name)
		# if "id" in self.__dict__ and self.__dict__["id"] is not None:
		# 	# pass##print("SAVINGGGG",self.id
		# 	GD.SaveX(self.pre+key,val)
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("111111111","Saving",key,"=",val,"111111111")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	pass##print("2222222222222222222222222222")
		# 	if key not in self.skip:
		# 		if key not in self.binded:
		# 			self.__dict__[key] = GD.bind(self.pre+key)
		# 			self.binded.append(key)
		# 	else:
		# 		self.__dict__[key] = val
		#
		# else:
		# 	self.__dict__[key] = val



		if not name.startswith("_") and "val" in self.__dict__ and name is not "val":# and "__skip" in self.__dict__ and name not in self.skip:
			if "obj.obj" not in str(type(value)):
				if name not in self.__dict__:
					pass##print("1",name)
					self.__dict__[name] = obj(id = self._id+"/"+name, val = value)
				else:
					pass##print("2",name)
					self[name].set(value)

				# if name not in self._binded:
				# 	self.__dict__[name].set(GD.bind(self._id+"/"+name))
				# 	self._binded.append(name)

				# GD.SaveX(self._id+"/"+name,value)
			else:
				self.__dict__[name] = value

		else:
			pass##print("3",name)
			self.__dict__[name] = value

	def __getattribute__(self, name, loop = True):
		if "str" not in str(type(name)):
			name = str(name)
		atr = object.__getattribute__(self, name)
		return atr

	def __getattr__(self, name, loop = True):
		if "str" not in str(type(name)):
			name = str(name)
		pass##print("getttt")
		# return name
		if not name.startswith("_") and "val" in self.__dict__ and name is not "val" and name not in self.__dict__:
			self[name] =  obj(id = self._id+"/"+name)
		if name in self.__dict__:
			atr = object.__getattribute__(self, name)
			# if name is "val" and "list" in str(type(atr)) and len(atr) is 1:
			if name is "val":# and "list" in str(type(atr)) and len(atr) is 1:
				return atr[0]
			return atr
		# return 13
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx",name)

	def set(self, val, count = 0 , max = 3):
		GD = obj.GD
		GD.SaveX(self._id,val)
		saved = GD.GetX(self._id)
		if saved != val and count<max:
			# print("trying again...")
			# print("trying again...")
			print("trying again...",saved,val)
			# print()
			self.set(val,count = count+1)

		# else:
			# print("Saved WORKED!!!!")
			# print("Saved WORKED!!!!")
			# print("Saved WORKED!!!!")


		# self.val = val
	def compareLists(self, ListA, ListB):
		added = []
		removed = []
		for b in ListB:
			if b not in ListA:
				added.append(b)
		for a in ListA:
			if a not in ListB:
				removed.append(a)
		return added,removed


	def __get__(self, obj=None, objtype=None):
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print(self, "$$$$", obj, "####", objtype)
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		return self
		return dict(self.__dict__)

	def __getstate__(self):
		print ("I'm being pickled")
		pass##print(self.__dict__)
		pass##print()
		return self.__dict__
		return False

	def __setstate__(self, d):
		pprint ("I'm being unpickled with these values:", d)
		self.__dict__ = d
		# self.val *= 3

	def inner(self, o):
		if "list" in str(type(o)) and len(o) is 1:
			return o[0]
		return o

	def __repr__(self):
		# return self.__str__()
		# pass##print("RRRRRRRRRRRRRR")
		# pass##print("RRRRRRRRRRRRRR")
		# pass##print("RRRRRRRRRRRRRR")
		# expand = self.__expand
		if time.time()-obj.expand<obj.expand_gap:
			# expand = False
			# if "_obj__expand" in self.__dict__:
				# self.__dict__.pop("_obj__expand")
			dic = dict( [(x,self.inner(y)) for x,y in self.__dict__.items() if not x.startswith('_')] )

			# dic = map(lambda x : self.inner(x), dic)
			# dic = dict( [(x,y) for x,y in self.__dict__.items() if not x.startswith('_')] )
			# expanded = str(dict(self.__dict__))
			expanded = str(dic)
			# obj.expand = False
			# pass##print("FFFFFFFF")
			return expanded

		v = dict(self.__dict__)["val"]
		if "list" in str(type(v)) and len(v) is 1:
			vv = dict(self.__dict__)["val"][0]
		else:
			vv = v
		if "str" in str(type(vv)):
			return str(vv)
			# return vv+"VVvvvvv"
		# vv = str(vv)+"++++++++++++"
		vv = str(vv)
		return vv

		return str({"val":self.val})
		return str(self.val)+", "+str(self.__dict__)
		return str([self.val, self.__dict__])

	def keys(self):
		return list(dict(self.__dict__))

	def checkStringRecr():
		pass

	# obj.expand_gap = 0.5
	def __str__(self):
		# pass##print("SSSSSSSSSSSSSS")
		# pass##print("SSSSSSSSSSSSSS")
		# pass##print("SSSSSSSSSSSSSS")
		# obj.expand = True
		obj.expand = time.time()
		# if "_obj__expand" in self.__dict__:
			# self.__dict__.pop("_obj__expand")		# return str(self.val)+" ___ S"

		# expanded = str(dict(self.__dict__))
		# d = {"test":[1],"b":[2]}
		# dic =dict( [(x,inner(y)) for x,y in d.items() if not x.startswith('_')] )
		# di = map(lambda x : x, dic)
		#
		dic = dict( [(x,self.inner(y)) for x,y in self.__dict__.items() if not x.startswith('_')] )
		# dic = dict(map(lambda x : self.inner(x), dic))
		expanded = str(dic)

		# expand = False
		return expanded
		return str({"val":self.val})
		return str(self.val)
		return str(self.__get__())

	def inner(o):
		if "list" in str(type(o)) and len(o) is 1:
			return o[0]
		return o

	def inner(self, o):
		if "list" in str(type(o)) and len(o) is 1:
			return o[0]
		return o

	def __is__(self, other):
		return self.__eq__(other)

	# by value of main
	def __eq__(self, other):
		if self.__isObj(other):
			return self.val[0] == other.val[0]
		elif "str" in str(type(other)):
			return str(self.val[0]) == other
		return self.val[0] == other

	def __add__(self, other):
		# pass##print("!!!!!!!!!")
		# pass##print(type(other))
		# pass##print()
		if self.__isObj(other):
			return self.val[0] + (other.val[0])
		elif "str" in str(type(other)):
			return str(self.val[0]) + other
		return self.val[0] + (other + 0)

	def __pos__(self, other):
		# pass##print("!!!!!!!!!")
		# pass##print(type(other))
		# pass##print()
		if self.__isObj(other):
			return self.val[0] + (other.val[0] + 0)
		elif "str" in str(type(other)):
			return str(self.val[0]) + other
		return self.val[0] + (other + 0)

	def __sub__(self, other):
		# pass##print("!!!!!!!!!")
		pass##print(type(other))
		pass##print()
		if self.__isObj(other):
			return self.val[0] - other.val[0]
		elif "str" in str(type(other)):
			pass##print("::::::::::::::xxxx:::::::::")
			return str(self.val[0]) - other
		return self.val[0] - other

	def __neg__(self, other):
		# pass##print("!!!!!!!!!")
		# pass##print(type(other))
		# pass##print()
		if self.__isObj(other):
			return self.val[0] + other.val[0]
		elif "str" in str(type(other)):
			return str(self.val[0]) + other
		return self.val[0] + other

	def __mul__(self, other):
		# pass##print("!!!!!!!!!")
		# pass##print(type(other))
		# pass##print()
		if self.__isObj(other):
			return self.val[0] * other.val[0]
		elif "str" in str(type(other)):
			return str(self.val[0]) * other
		return self.val[0] * other

	def __truediv__(self, other):
		# pass##print("!!!!!!!!!")
		# pass##print(type(other))
		# pass##print()
		if self.__isObj(other):
			return self.val[0] / other.val[0]
		elif "str" in str(type(other)):
			return str(self.val[0]) / other
		return self.val[0] / other

	def is_(self,other):
		pass##print("IISSSSSSSSSSSSSSSSSSSSSSSSSSSSISISISIS")
		if self.__isObj(other):
			return self.val[0] == other.val[0]
		return self.val[0] == other

	def __isObj(self, o):
		return "obj.obj" in str(type(o))

	def __call__(self, *vars):
		pass##print(":::::::::::::::::::::::")
		for v in vars:
			pass##print(v)
		pass##print(":::::::::::::::::::::::")



fuckYea = obj(17)

#expando.py



from pprint import *
import os, time

#
# class ext(dict):
# 	def __init__(self):
# 		self._x = "xxxxxxxxx"
#
# 	def x(self):
# 		print(self._x)


import readline
import re
import inspect
from threading import Thread
import traceback, threading, time

class InstanceCreationError(Exception):
	pass

#class RememberInstanceCreationInfo:



import readline
import re

class SomeObject():
	def __init__(self):
		cmd = readline.get_history_item(readline.get_current_history_length())
		self.name = re.split('=| ',cmd)[0]

import collections


import traceback


x,y,z = 1,2,3

def retrieve_name(var):
	callers_local_vars = inspect.currentframe().f_back.f_locals.items()
	return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def mod_retrieve_name(var):
	callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
	return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def foo(bar):
	print (retrieve_name(bar))
	print (mod_retrieve_name(bar))

foo(x)


# def makeObj():


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



class ex(RICI):
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
			print("APSCmOSKMCLKLAMSCKMSPCM")
			cmd = readline.get_history_item(readline.get_current_history_length())
			print("cmd",cmd)
			self.name = re.split('=| ',cmd)[0]
			print("!!!",self.name)
		else:
			self.name = self.creation_name
		return self.name
	# def __init__(self, id = None, val = None):#, wrapper = False, main = True):
	def foo(self):
		print ("#### ",retrieve_name(self))
		print ("#### ",mod_retrieve_name(self))



	def get_my_name(self):
		ans = []
		frame = inspect.currentframe().f_back
		frame = inspect.currentframe().f_back.f_back
		# print()
		# print()
		# print()
		# print()
		# print()
		# print()
		# print("@@@@@@@@@@@@@")
		# print(frame.f_globals.items(), frame.f_locals.items())
		# print("@@@@@@@@@@@@@")
		tmp = dict(frame.f_globals.items())
		for i in frame.f_locals:
			tmp[i] = frame.f_locals[i]
		# tmp.append()
		for k, var in tmp.items():
			# if isinstance(var, self.__class__):
			if isinstance(var, collections.Hashable):

				if hash(self) == hash(var):
					ans.append(k)
		return ans

	def makeID(self, args = []):
		t = time.time()

		# while('self' == self.get_my_name()[0] and time.time()-t<4):
		# 	print("...")
		# print(time.time()-t,"******---",self.get_my_name())
		# print("******---",self.get_my_name())
		# print("******---",self.get_my_name())
		#
		# self["_id"] = self.get_my_name()[0]self.get_my_name()

	def check(self):
		self.validID()
		print("@@@@@@@@@@@@@@@",self._id, self.xxx)

	def validID(self):
		if not self.__validID__:
			print("xxx")
			if 'self' != self.get_my_name()[0]:
				self._id = self.get_my_name()[0]
				self.__validID_ = True
				print("!!!!!!!!!!!!!!!!!!!")
			else:
				self._id = self.get_my_name()[0]



	def __init__(self, val = "__17__", main = True, **entries):#, wrapper = False, main = True):
#expando.py
		# def __init__(self):
		# es=traceback.extract_stack()
		super().__init__()
		self.name = self.GetName()
		self.__dict__.update(entries)
		self.__validID_ = False
		# global GD
		# self.xxx = self.get_my_name()
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
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

	def __setattr__(self, name, value):
		if not name.startswith("_") and "val" in self.__dict__ and name is not "val":# and "__skip" in self.__dict__ and name not in self.skip:
			if "ex.ex" not in str(type(value)):
				if name not in self.__dict__:
					self[name] = ex(value)
				else:
					self[name].set(value)
			else:
				self.__dict__[name] = value

		else:
			self.__dict__[name] = value

	def __getitem__(self, name):

		if not name.startswith("_") and "val" in self.__dict__ and name is not "val" and name not in self.__dict__:
			self.__dict__[name] = ex()
		if name in self.__dict__:
			item = self.__dict__[name]
			return item

			atr = object.__getattribute__(self, name)
			return atr



	def __setitem__(self, name, value):
		if not name.startswith("_") and "val" in self.__dict__ and name is not "val":# and "__skip" in self.__dict__ and name not in self.skip:
			if "ex.ex" not in str(type(value)):
				if name not in self.__dict__:
					print("1",name)
					self.__dict__[name] = ex(value)
				else:
					print("2",name)
					self[name].set(value)
			else:
				self.__dict__[name] = value
		else:
			print("3",name)
			self.__dict__[name] = value

	def __getattribute__(self, name, loop = True):
		atr = object.__getattribute__(self, name)
		return atr
	def __getattr__(self, name, loop = True):
		print("getttt")
		# return name
		if not name.startswith("_") and "val" in self.__dict__ and name is not "val" and name not in self.__dict__:
			self[name] = ex()
		if name in self.__dict__:
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

	def __get__(self, obj=None, objtype=None):

		return self
		return dict(self.__dict__)

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
		return str({str(self.name):self.val})

		return str({"val":self.val})
		return str(self.val)+", "+str(self.__dict__)
		return str([self.val, self.__dict__])

	# def

	def __str__(self):
		return str({str(self.name):self.val})
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
			return self.val + other.val
		elif "str" in str(type(other)):
			return str(self.val) + other
		return self.val + other

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
			return self.val - other.val
		elif "str" in str(type(other)):
			print("::::::::::::::xxxx:::::::::")
			return str(self.val) - other
		return self.val - other

	def __neg__(self, other):
		# print("!!!!!!!!!")
		# print(type(other))
		# print()
		if self.__isObj(other):
			return self.val + other.val
		elif "str" in str(type(other)):sr
		return self.val + other

	def __isObj(self, o):
		return "ex.ex" in str(type(o))

	def __call__(self, *vars):
		print(":::::::::::::::::::::::")
		for v in vars:
			print(v)
		print(":::::::::::::::::::::::")



def new():
    yes =  ex(111)
    return yes
wow = new()

from rici import *
class MySubclass(RICI):
	def __init__(self):
		super().__init__()

	def print_creation_info(self):
		print(self.creation_name, self.creation_module, self.creation_function,
		self.creation_line, self.creation_text, sep=", ")

# instance = MySubclass()
# instance.print_creation_info()
#out: instance, __main__, <module>, 68, instance = MySubclass()


import inspect
class A(object):
	def get_my_name(self):
		ans = []
		frame = inspect.currentframe().f_back
		print()
		print()
		print()
		print()
		print()
		print()
		print("@@@@@@@@@@@@@")
		print(frame.f_globals.items(), frame.f_locals.items())
		print("@@@@@@@@@@@@@")
		tmp = dict(frame.f_globals.items())
		for i in frame.f_locals:
			tmp[i] = frame.f_locals[i]
		# tmp.append()
		for k, var in tmp.items():
			if isinstance(var, self.__class__):
				if hash(self) == hash(var):
					ans.append(k)
		return ans

def test():
	a = A()
	b = a
	c = b
	print (c.get_my_name())

test()

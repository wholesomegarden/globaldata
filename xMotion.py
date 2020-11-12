
from gd import *
import re


a = '''hello? there A-Z-R_T(,**), world, welcome to python.
this **should? the next line#followed- by@ an#other %million^ %%like $this.'''


### xo.key = "bcc"
### xo.showKey()

txt = "a b c d a b c d "

txt = 'Daylight saving time (DST), also daylight savings time or daylight time (United States and Canada) and summer time (United Kingdom, European Union, and others), is the practice of advancing clocks during warmer months so that darkness falls later each day according to the clock. The typical implementation of DST is to set clocks forward by one hour in the spring ("spring forward") and set clocks back by one hour in autumn ("fall back") to return to standard time.[1][2] In other words, there is one 23-hour day in late winter or early spring and one 25-hour day in the autumn.'
txt = 'time The typical implementation of DST time is to set clocks forward by one hour in the spring ("spring forward") and set clocks back by one hour in autumn'

#db = xo.bigggxxxxx
key = xo.bigggxxxxx._id

txt = "a b c d r a b c d b c f b c f b c z b c x b c y b c x"


#db = xo.bccc
key = xo.bccc._id

txt = "all having fun"
key = xo.feelingood._id

print()
print()
print("PLEASE PASTE TXT:")
txt = cleantxt(input().replace("\'","")
key = xo.input._id

xo.key = key


db = xo[key]

#xo.key = "bccc"




txt.replace("-"," ")
txt.replace("("," ")
txt.replace(")"," ")



dict = txt.split(" ")
tt = time.time()

for a in dict:
	print(a)

M = {}

def dictMag(xobj):
	pass

def addW(w,i,dict,M):
	time.sleep(.0001)
	if i is not 0:
		pass	
		#print("PREV::::",dict[i-1],M[dict[i-1]])
	if w not in M.__dict__.keys():
		M[w] = [i]
		#print('aa.      ',w,M[w].val)
#	elif W in M
	else:
		#print('bb.      ',w,M[w].val)
		foundPrev = False
		prevs = M[w].val[0]
		for p in prevs:
			#print("AAAAAAAAAAA",p)
			#time.sleep(1)
			if True:
				#print("BBBBBBBBBBBBBBBBB")
				if p != 0 and i != 0 and p != i:
					#print("CCCCCCCCCCCCCCC",p)
					pw = dict[p-1]
					#print(pw,"!!!!!!!!!!!!")
					if pw == dict[i-1]:
						#print("FOUND SAME PREV")
						foundPrev = True
						addW(pw+"/"+w,p-1,dict,M)
				else:
					#print("DDDDDDDDDDDDDD")
					pass#print("!!!",p,i)
			else:
				pass #print("PPPPPPPP",p)
		if foundPrev:
			pass#M[dict[i-1] + " " + w].append(i-1)
			if i != 0:
				addW(dict[i-1] + "/" + w,i-1,dict,M)
		else:
			pass #print("not found",w)
		#print("XXXXXXX")
		#time.sleep(.3)
		if i not in M[w].val[0]:
			
			#time.sleep(0.5)
			#print("XXXXXXX")
			#print("/////////",w)
			arr = M[w].val[0]
			arr.append(i)
			M[w] = arr
		#print("XXXXXXX")	

	return M

def getConnections(dict, M):
	for i in range(len(dict)):
		#time.sleep(1)
		w = dict[i]
		print("===========",w, i)
		addW(w,i,dict,M)
#	return M



getConnections(dict,db)
#time.sleep(3)

print("!!!!!!!!!!!!")
print(txt)
print("!!!!!!!!!!!!")
print(M)

print()


for a in M:
	print(a,M[a])

print("Done",time.time()-tt," seconds - for ",len(dict), "words - avg.=",(time.time()-tt)/(len(dict)), "per word")


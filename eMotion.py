

txt = "a b c d a b c d "

dict = txt.split(" ")


for a in dict:
	print(a)

M = {}

def addW(w,i,dict,M):
	print("::::::::  adding",i, w)
	if w not in M:
		M[w] = [i]
#	elif W in M
	else:
		foundPrev = False
		for p in M[w]:
			if p != 0 and i != 0 and p != i:
				pw = dict[p-1]
				if pw == dict[i-1]:
					print(":::::::::::::::: FOUND SAME PREV")
					foundPrev = True
					addW(pw+" "+w,p-1,dict,M)
			else:
				pass#print("!!!",p,i)
		if foundPrev:
			pass#M[dict[i-1] + " " + w].append(i-1)
			if i != 0:
				addW(dict[i-1] + " " + w,i-1,dict,M)
		else:
			print(":::::::::::: not found",w)

		if i not in M[w]:
			print(":::::::::::://///////",w)
			M[w].append(i)		

	return M

def getConnections(dict, M):
	for i in range(len(dict)):
		w = dict[i]
		print("::::",i, w)
		addW(w,i,dict,M)
	return M



con = getConnections(dict,M)

print("!!!!!!!!!!!!")
print(txt)
print("!!!!!!!!!!!!")
print(M)

print()
for a in M:
	print(a,M[a])




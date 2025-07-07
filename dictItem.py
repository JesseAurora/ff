# ff merge usage
import re
countDict={}
f = open("/Users/Jesse/.recentlyAccess")
for line in f.readlines():
	try:
		line=line.strip('\n')
        # replace more than space to one space
		arr=re.sub(' +',' ',line).split(" ")
		if arr[2] in countDict.keys():
			countDict[arr[2]]=int(countDict.get(arr[2]))+int(arr[1])
		else:
			countDict[arr[2]]=int(arr[1])
	except Exception as e:
		pass

f.close()

for (k,v) in countDict.items():
	print("   "+str(v)+" "+k)

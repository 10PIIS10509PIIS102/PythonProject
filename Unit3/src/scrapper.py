import re
import linecache

f=open('input.txt','r')
w= open('input2.txt','a')
i=0
for line in f.readlines():
	i=i+1
	if re.match('[0-51].[a-z]+-',line,re.I):
		w.write('\nTourist places\n')
		w.write(line)
	elif re.match('[a-z]+-[a-z]+',line,re.I):
		w.write('\nhotels\n')
		w.write(line)
	elif re.match('[a-z]+:-',line,re.I):
		w.write('\nHill stations\n')
		w.write(line)
		#sss=linecache.getline('input.txt',i+1)
		sss=f.readline()
		w.write(sss)
	elif re.match('[a-z]+Beach(,)?([a-z]+)?',line,re.I):
		w.write('\nBeach\n')
		w.write(line)
f.close()
w.close()

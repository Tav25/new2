#!/usr/bin/env python
# -*- coding: utf-8 -*-
fil='spisES.txt'
i=0
x=[]
y=[]
for line in open(fil):
        f=line
        if not f in x:
                
                #y.append(f)
                #print('x:_'+str(x))
                #print('y:_'+str(y))
                #d=input()
                #sl='dctc'+'\n'
                sl=f
                i2=0
                for line in open(fil):
                        if sl==line:
                                i2=i2+1
                                #print(i2)
                if i2>50:
                        x.append(f)
                        y.append(i2)
        i=i+1
	#print(line)
#print(i)
#print(len(x))
#print(len(y))
#print(x)
#print(y)
#print(max(y))

print(y.index(max(y)))#slovo
print(x[y.index(max(y))])#kolichestvo
xy=[]
i3=0
while len(x)>i3:
	i3+=1
	#print(y.index(max(y)))
	xy.append(str(max(y))+x[y.index(max(y))])
	y[y.index(max(y))]=0


input()

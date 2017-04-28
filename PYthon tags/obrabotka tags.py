#!/usr/bin/env python
# -*- coding: utf-8 -*-
fil='spis.txt'
i=0
x=[]
y=[]
for line in open(fil):
        f=line
        if not f in x:
                sl=f
                i2=0
                for line in open(fil):
                        if sl==line:
                                i2=i2+1
                                #print(i2)
                if i2>1:#
                        x.append(f)
                        y.append(i2)
        i=i+1
print(y.index(max(y)))#slovo
print(x[y.index(max(y))])#kolichestvo
xy=[]
i3=0
f = open('vuhod.txt','w')
while len(x)>i3:
	i3+=1
	#print(y.index(max(y)))
	xy.append(str(max(y))+x[y.index(max(y))])
	y[y.index(max(y))]=0
	#f.write(x[y.index(max(y))][0:-2]+', ')
	f.write(x[y.index(max(y))])
f.close()
input()


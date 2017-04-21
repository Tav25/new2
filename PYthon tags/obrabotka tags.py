#!/usr/bin/env python
# -*- coding: utf-8 -*-
fil='spisES.txt'
i=0
x=[]
y=[]
for line in open(fil):
        f=line
        if not f in x:
                x.append(f)
                #y.append(f)
                #print('x:_'+str(x))
                #print('y:_'+str(y))
                #d=input()
                sl='Disney Baby Toys'+'\n'
                i2=0
                for line in open(fil):
                        if sl==line:
                                i2=i2+1
                                print('!!!')
                y.append(f)
        i=i+1
	#print(line)
#print(i)
print(len(x))
print(len(y))
#print(f)


sl='Disney Baby Toys'+'\n'
for line in open(fil):
        if sl==line:
                print('!!!')
input()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('''
tegi dla SJ
_____________________________________
''')
import random
x1=['huevos sorpresa','juguetes','huevos kinder','huevo sorpresa','huevo kinder','videos para niños','huevos sorpresa en español','surprise eggs','egg surprise','en español']#теги 1категории
x2=['juguete','surprise egg','pelicula en español','videos de juguetes','sorpresa en español','toy','kinder en español','videos en español','video en español','eggs surprise','kinder eggs','peliculas en español','sorpresas en español','kinder surprise','kinder egg']#теги 2категории
x3=['surprise','kinder sorpresa','peppa pig','disney','oeufs','ovos','huevo sorpresa en español','videos de huevos','juguetes sorpresa','kinder joy','videos para bebes','videos de huevos sorpresa','huevo sorpresa kinder','Kinder Surprise (Consumer Product)']#теги 2категории
big=[]

x = len(x1)#список откуда берем теги
x0=x1#х0 присмаеваем список
i=0#счетчик
r0=[]#список для проверки рандом чисел
while i<x:
	r1=random.randint(0, x-1);#случайное число 
	#r0.append(r1) 
	if not r1 in r0:#проверям если случ в списке
		#print('+++')
		r0.append(r1)
		big.append(x0[r1])
		i+=1;		
	
#print(r0);

x = len(x2)
del r0[:]
x0=x2
i=0
r0=[]
while i<x:
	r1=random.randint(0, x-1);
	#r0.append(r1) 
	if not r1 in r0:
		#print('+++')
		r0.append(r1)
		big.append(x0[r1])
		i+=1;		
#print(r0);

x = len(x3)
del r0[:]
x0=x3
i=0
r0=[]
while i<x:
	r1=random.randint(0, x-1);
	#r0.append(r1) 
	if not r1 in r0:
		#print('+++')
		r0.append(r1)
		big.append(x0[r1])
		i+=1;		
#print(r0);

#print(big)

kolsimv=''
big_x = len(big)
f = open('tags_SJ.txt','w')
i=0
w=input('kolichestvo simvolov: ')
while i<big_x:
        kolsimv+=big[i]
        #print(len(kolsimv))
        if len(kolsimv)>w:
                break
        f.write(big[i]+', ')
        i+=1;
#f.write('222')
f.close()
input('...OK') 

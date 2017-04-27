#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('''
tegi dla SJ
_____________________________________
''')
import random
x1=['for kids','nursery rhymes','colors','cartoon','cars','for Children','cars cartoon']#теги 1категории
x2=['color','learn colors','transportation','children','truck','learn','cartoon','cartoon for kids','Colors for Children','songs','kids','color cars','colors for kids']#теги 2категории
x3=['learning video','learn numbers','cars for kids','learning','for Toddlers','fun','numbers','funny','cars transportation','Monster Truck','Nursery Rhymes Songs','superhero','bus','superheroes','trucks','video','car','Cars Cartoon for Kids','Mack truck','for Kids','Colors for Toddlers','long cars','police cars','Small','vehicles','cartoon for children','Children Songs','colors cars','helicopter','Learn Color']#теги 3категории
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
f = open('tag.txt','w')
f2 = open('tit.txt','w')

i=0
w=input('kolichestvo simvolov: ')
while i<big_x:
        kolsimv+=big[i]
        if len(kolsimv)<20:
                print('2')
                f2.write(big[i]+'. ')
        if len(kolsimv)>w:
                break
        f.write(big[i]+', ')
        i+=1;
f.write('SJ_channel,')
#f.write('222')
f.close()
f2.close()
#dis
f3 = open('dis.txt','w')
f3.write('''Like and Subscribe: https://www.youtube.com/channel/UCkrwtYHbL-CdAdhB3hgvhtQ?sub_confirmation=1

Colors Cars for Children   Sj Channel!!!

Video created with the purpose of learning and development of children!''')
input('...OK') 

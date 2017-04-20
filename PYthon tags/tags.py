print('''
tegi dla SJ
_____________________________________
''')
import random
x1=['for kids','nursery rhymes','spiderman','colors','spiderman cartoon','cars''for Children','cars cartoon']
x2=['color','learn colors','transportation','children','truck','learn','cartoon','lightning mcqueen','cartoon for kids','Colors for Children','songs','kids','color cars','colors for kids']
x3=['learning video','learn numbers','cars for kids','learning','for Toddlers','fun','numbers','funny','cars transportation','Spiderman Cartoon for kids','mcqueen','Monster Truck','Nursery Rhymes Songs','superhero','bus','superheroes','trucks','video','car','Cars Cartoon for Kids','Mack truck','Spiderman for Kids','Colors for Toddlers','long cars','Batman','police cars','Small','vehicles','cartoon for children','Children Songs','colors cars','helicopter','Learn Color','spiderman carton']
big=[]

x = len(x1)
x0=x1
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
f = open('tags.txt','w')
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
input('***')

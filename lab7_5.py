#! /usr/bin/env python3


b=input('Zadaite ryadok : ')

a=str.lower(b)

i=0

g=0

while i<len(a):
	
  if (a[i]=='a') or (a[i]=='o') or (a[i]=='u') or (a[i]=='i') or (a[i]=='e') or (a[i]=='y'):
		
    g +=1
	
  i=i+1



print('Golosnux bykv ',g)
#! /usr/bin/env python3


b=input('Zadaite ryadok : ')

c=b[::]

k=input('Zadaite dovzuny zsyvy')

if int(k)>len(b)/2:
   
   print('k ne moze bytu bil6wum za polovuny r9dka')

new=''

new=c[k+1:len(c)]+c[0:k+1]

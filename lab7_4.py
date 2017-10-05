#! /usr/bin/env python3

def wifr(a):
  
  new=''
  
  for i in a:
    
    new=new+chr(ord(i)+1)
  
  return new

a=input('zadaite r9dok ')

print('Zashufrovanui r9dok : ',wifr(a))
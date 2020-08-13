# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:42:07 2020

@author: Lujain Ararawi
"""

n=int(input("Please insert the number of propositions> "))
for i in range(1,n+1):
    print("P" +str(i) ,end="     ")
print()
print("-" *(5*n))
r=int(2**n)
L=[]
while r!=1:
    L.append((r//2)*["F" ]+(r//2)*["T" ])
    r//=2
r=int(2**n)
for i in range(len(L)):
    L[i]=(r//len(L[i]))*L[i]
i=0
j=0
while i<r:
    for k in L:
        print(k[j],end="      ")
    print()
    j+=1
    i+=1
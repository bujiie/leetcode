#!/usr/bin/env python3

from sys import argv


N=[]
with open(argv[1]) as fp:
    for l in fp:
        l=l.strip()
        N=[int(n) for n in l.split(',')]

    
def moveZeroes(nums):
    if len(nums) < 2:
        return

    z=[]
    nz=[]
    for n in nums:
        if n==0:
            z.append(0)
        else:
            nz.append(n)

    result=nz+z
    for i in range(len(nums)):
        nums[i]=result[i]
        
moveZeroes(N)
print(N)      

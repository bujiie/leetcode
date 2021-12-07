#!/usr/bin/env python3

from sys import argv

N=[]
k=0
with open(argv[1]) as fp:
    for i,l in enumerate(fp):
        l=l.strip()
        if i==0:
            N=[int(n) for n in l.split(',')]
        else:
            k=int(l)

def rotate(nums, k):
    l=len(nums)
    
    # any amount of rotation will result in the
    # same single entry list.
    if l==1:
        return

    # when k==len(nums) that means we have reached
    # the end of the list and need to start over
    # again. we can ignore these start overs because
    # it puts us in the same place as the original
    # start position. we use modulo operator to get
    # us the remaining k that we need to worry about.
    if k > l:
        k=k%l

    # because of the way we slide the nums list, we
    # need to special case k==1. when we slice the
    # list, [:n] will only result values if n>0.
    if k==1:
        left,right=nums[:-k],[nums[-1]]
    else:
       left,right=nums[:1-k],nums[-k:]

    # this is the main "rotate" part of the algorithm.
    # instead of shifting values individually, we just
    # grab the two pieces, left and right of the
    # rotation point k and swap places.
    result=right+left


    # we have to overwrite each entry in nums
    # because we cannot reassignment will not
    # affect the nums variable outside the
    # scope of this function.
    for i in range(l):
        nums[i]=result[i]

rotate(N, k)
print(N)

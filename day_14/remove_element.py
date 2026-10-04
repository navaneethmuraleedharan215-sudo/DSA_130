nums=[3,2,2,3]
def removeElement(nums,val):
    i=0
    n=len(nums)
    while i< n:
        if nums[i]==val:
            nums[i]=nums[n-1]
            n-=1
        else:
            i+=1

    return n
n=removeElement(nums,val=2)
print(n)
print(nums[:n])
nums=[1,1,2,3,3,3,4,5]
def removeDuplicates(nums):
    if not nums:
        return 0
    l=1
    for r in range(1,len(nums)):
        if nums[r]!= nums[r-1]:
            nums[l]=nums[r]
            l+=1
    return l
print(removeDuplicates(nums))
print(nums[:5])



   


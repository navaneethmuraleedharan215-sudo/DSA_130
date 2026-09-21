def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

nums=[10,1,5,4]
target=15
print(twosum(nums, target))


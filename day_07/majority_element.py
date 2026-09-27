nums=[2,1,2]
def majority(nums):
    nums.sort()
    n=len(nums)
    return nums[n//2]


print (majority(nums))
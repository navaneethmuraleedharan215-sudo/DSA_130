nums=[0,1,3,5,0,6]
def movezeroes(nums):
    n=len(nums)
    for i in range(n):
        if 0 in nums:
            nums.append(nums.pop(nums.index(0)))
    return nums
print(movezeroes(nums))
nums=[2,3,1,2,4,3]
target=7
def minSubArrayLen(target,nums):
    min_length=float('inf')
    summ=0
    l=0

    for r in range(len(nums)):
        summ+=nums[r]

        while summ>=target:
            min_length=min(min_length,r-l+1)
            summ-=nums[l]
            l+=1

    return min_length if min_length<float('inf')else 0

print(minSubArrayLen(target,nums))
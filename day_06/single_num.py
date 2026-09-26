nums=[2,1,3,1]
def SingleNum(nums):
    result=0
    for n in nums:
        result^=n
    return result
print(SingleNum(nums))

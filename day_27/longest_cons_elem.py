def LongestConsecutive(nums):
    s=set(nums)
    longest=0
    for num in nums:
        if num-1 not in s:
            next_num=num+1
            length=1
            while next_num in s:
                length+=1
                next_num+=1
            longest=max(longest,length)
    return longest

nums=[100,1,2,200,3,4]
print(LongestConsecutive(nums))
nums=[2,0,2,1,1,0]
def Sortcolors(nums):
    counts=[0,0,0]

    for color in nums:
        counts[color]+=1

    R,W,B=counts
    nums[:R]=[0]*R
    nums[R:R+W]=[1]*W
    nums[R+W:]=[2]*B
    return nums

print(Sortcolors(nums))
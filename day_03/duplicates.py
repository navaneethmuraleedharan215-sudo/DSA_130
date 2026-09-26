nums=[2,1,4,2]
duplicates={}
result=False
for n in nums:
    if n in duplicates:
        result=True
        break
    else:
        result=True

print(result)
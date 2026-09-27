digits=[4,3,2,1]
def plusone(digits):
    for i in range(len(digits)):
        if digits[i]+1!=10:
          digits[i]+=1
          return digits
        
print(plusone(digits))



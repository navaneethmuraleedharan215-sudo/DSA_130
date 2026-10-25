from collections import defaultdict
fruits=[1,2,1]
def totalFruit(fruits):
    count=defaultdict(int)
    total,res=0,0
    for r in range(len(fruits)):
        count[fruits[r]]+=1
        total+=1

        while len(count)>2:
            f=fruits[l]
            count[f]-=1
            total-=1
            l+=1
            if not count[f]:
                count.pop(f)

        res=max(res,total)
    return res

print(totalFruit(fruits))
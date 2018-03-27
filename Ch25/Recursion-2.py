def groupSum(start, x, target):
    if target == 0:
        return True
    if start == len(x):
        return False
    return groupSum(start+1, x, target = target - x[start]) or groupSum(start + 1, x, target)

print(groupSum(0,[1,2,3],7))

def groupSum6(start, x, target):
    if start == len(x):
        return (target == 0)
    if x[start] == 6:
        return groupSum6(start+1, x, target = target - x[start])
    else:
        return groupSum6(start + 1, x, target=target - x[start]) or groupSum6(start + 1, x, target)

print(groupSum6(0,[1,2,3,6],7))

def groupNoAdj(start, x, target):
    if start+1 > len(x):
        return (target == 0)
    return groupNoAdj(start + 2, x, target=target - x[start]) or groupNoAdj(start + 1, x, target)

print(groupNoAdj(0,[4,3,2,7],9))

def groupSum5(start, x, target):
    if start+1 > len(x):
        return (target == 0)
    if x[start]%5 == 0 and x[start+1]==1:
        return groupSum5(start + 2, x, target - x[start])
    elif x[start]%5 == 0:
        return groupSum5(start+1, x, target - x[start]) 
    return groupSum5(start+1,x,target - x[start]) or groupSum5(start + 1, x, target)

print(groupSum5(0,[10,5,2,1,4],16))

def groupSumClump(start, x, target):
    if start + 1 > len(x):
        return (target == 0)
    if start < len(x) -1:
        if x[start] == x[start+1]:
            i = start
            while i < len(x) -1 and x[i] == x[i+1]:
                i+=1
            i+=1
            return groupSumClump(i, x , target) or groupSumClump(i, x, target - (i-start)*x[i-start])
    return groupSumClump(start+1,x,target - x[start]) or groupSumClump(start + 1,x, target)

print(groupSumClump(0,[1,2,2,2,4,6],2))

def splitArray(x,start=0,l=0,r=0):
    if start == len(x):
        return l == r
    return splitArray(x,start+1,l+x[start],r) or splitArray(x,start+1,l,r+x[start])

print(splitArray([5,2,3]))

def splitOdd10(x,start=0,l=0,r=0):
    if start == len(x):
        return (l%10==0 and r%2==1) or (l%2==1 and r%10==0)
    return splitOdd10(x, start + 1, l + x[start], r) or splitOdd10(x, start + 1, l, r + x[start])

print(splitOdd10([5,5,6,]))

def split53(x,start=0,l=0,r=0):
    if start == len(x):
        return l==r
    if x[start]%3==0:
        return split53(x,start+1,l,r+3)
    if x[start]%5==0:
        return split53(x,start+1,l+5,r)
    return split53(x,start+1,l+x[start],r) or split53(x,start+1,l,r+x[start])

print(split53([3,3,1,5,3,1]))


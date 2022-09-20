
from re import I


def search(nums,target) -> int:
    minIndex = nums.index(min(nums))
    numsT = nums[minIndex:] + nums[:minIndex]
    low = 0
    high  = len(numsT) - 1

    while True:
        i  = int((low + high) / 2)
        if target < numsT[i]:
            high = i - 1
        elif target > numsT[i]:
            low = i + 1
        elif target == numsT[i]:
            i += minIndex
            if i >= len(nums): i -= len(nums)
            break
        if low > high:
            i = -1
            break
    return i


def createInput():
    return [
        [0,[4,5,6,7,0,1,2]],
        [3,[4,5,6,7,0,1,2]],
        [0,[1]],
        [3,[3,1]]
    ]

NN = createInput()
for N in NN:
    print("===================")
    print(N)
    print(search(N[1],N[0]))
    print("===================")
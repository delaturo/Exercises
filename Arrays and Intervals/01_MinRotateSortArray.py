
def findMin(nums) -> int:
    i = 0
    min = nums[-1]
    while i < len(nums)-1:
        if nums[i-1] > nums[i] and nums[i] < nums[i+1]:
            min = nums[i]
            break
        i += 1
    return min

def createInput():
    return [
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17],
        [1],
        [2,1],
        [1,2]
    ]

NN = createInput()
for N in NN:
    print("===================")
    print(N)
    print(findMin(N))
    print("===================")
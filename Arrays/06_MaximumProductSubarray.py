
def maxProduct(nums):
    maxProd = nums[0]
    currentProd = [nums[0]]
    i = 1
    while i < len(nums):
        currentN = nums[i]

        currentProd = [n * nums[i] for n in currentProd if n != 0]
        if len(currentProd) == 0:
            currentProd.append(nums[i])
        else:
            if nums[i] < 0 or currentProd[-1] < 0:
                currentProd.append((nums[i] if nums[i] != 0 else 1))

        tmax = max(currentProd)
        if maxProd < tmax:
            maxProd = tmax
        elif maxProd < nums[i]:
            maxProd = nums[i]

    
        i += 1
    if maxProd == 0:
        maxProd = max(nums)
    
    return maxProd           

def createInput():
    return [
    [2,3,-2,4]
    ,[-2,0,-1]
    , [-2]
    , [0,2]
    , [-3,-1,-1]
    , [3,-1,4]
    , [-1,-2,-3,0]
    ,[1,0,-1,2,3,-5,-2]
    ]

NN = createInput()
for N in NN:
    print(maxProduct(N))


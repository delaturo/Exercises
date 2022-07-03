
def maxSubArray(nums):
    i = 0
    currentSum = 0
    maxSum = nums[i]
    while i < len(nums):
        currentN = nums[i]
        if currentSum + nums[i] < 0:
            currentSum = 0
            if nums[i] > maxSum:
                maxSum = nums[i]
        else:
            currentSum += nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
        i += 1
    return maxSum           

def createInput():
    return [
    [-2,1,-3,4,-1,2,1,-5,4] # Expected & explanation: [4,-1,2,1] has the largest output = 6.
    ,  [1]
    , [5,4,-1,7,8]
    , [1,2]
    , [-2,-1]
    , [1,2,-1,-2,2,1,-2,1,4,-5,4]
    , [0,-3,1,1]
    , [1,1,-2]
    , [3,2,-3,-1,1,-3,1,-1]
    , [-1,1,-3,-2,2,-1,-2,1,2,-3]
    , [0]
    , [-1,0]
    ]

NN = createInput()
for N in NN:
    print(maxSubArray(N))


import math
def productExceptSelf(nums):
    size = len(nums)
    res = [1] * size
    iL = 1
    iR = 1
    for i in range(len(nums)):
        j = size-1-i
        res[i] = res[i] *iL
        res[j] = res[j] *iR
        iL = iL* nums[i]
        iR = iR * nums[j]

    return res


def createInput():
    return [1,2,3,4]
    # return [-1,1,0,-3,3]

N = createInput()
print(productExceptSelf(N))

def twoSum(nums, target):
        for i in range(len(nums)-1):
            complement = target - nums[i]
            substring = nums[i+1:]
            if complement in substring:
                j = substring.index(complement)+i+1
                return [i, substring.index(complement)+i+1]

def createInput():
    # return [[2,7,11,15],9]
    # return [[3,2,4],6]
    return [[3,3],6]

N = createInput()
print(twoSum(N[0],N[1]))
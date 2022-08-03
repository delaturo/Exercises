
def threeSum(nums) -> int:
    res = []
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if j == i:
                continue
            for k in range(len(nums)-1):
                if k == j or k == i:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    # res.append([nums[i], nums[j], nums[k]]) 
                    toAdd = sort([i, j, k])

                    res.append([i, j, k])
    return res

def createInput():
    return [
        [-1,0,1,2,-1,-4]
    ]

NN = createInput()
for N in NN:
    print("===================")
    print(N)
    print(threeSum(N))
    print("===================")
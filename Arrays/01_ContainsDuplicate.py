
def containsDuplicate(nums) -> bool:
        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            else:
                numSet.add(n)
        return False

def createList():
    # return [1,2,3,1]
    # return [1,2,3,4]
    return [1,1,1,3,3,4,3,2,4,2]

N = createList()
print(containsDuplicate(N))

def insert(intervals, newInterval):
    xFound = mergeX = 0
    yFound = mergeY = 0
    xInt = None 
    yInt = None
    i = 0
    while i<len(intervals) and (not xFound or not yFound):
        if not xFound:
            if newInterval[0] > intervals[i][1]:
                xInt = i+1
            elif newInterval[0] < intervals[i][0]:
                xInt = i
                xFound = True
            elif intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[0]:
                mergeX = 1
                xInt = i
                xFound = True

        if not yFound:
            if newInterval[1] > intervals[i][1]:
                yInt = i+1
            elif newInterval[1] < intervals[i][0]:
                yInt = i
                yFound = True
            elif intervals[i][1] >= newInterval[1] and intervals[i][0] <= newInterval[1]:
                mergeY = 1
                yInt = i
                yFound = True
        i += 1

    if xInt == None:
        xInt = 0
    if yInt == None:
        yInt = 0

    interval = [0,0]
    if mergeX:
        interval[0] =  intervals[xInt][0]
    else:
        interval[0] = newInterval[0]
        
    if mergeY:
        interval[1] =  intervals[yInt][1]
    else:
        interval[1] = newInterval[1]

    i = 0
    yInt +=mergeY
    while (i< yInt - xInt):
        intervals.pop(xInt)
        i += 1
            
    intervals.insert(xInt, interval)

    return intervals


def createInput():
    return [
        ([[1,5]], [0,6]),
        ([],[5,7]),
        ([[1,5]],[6,8]),
        ([[1,3],[6,9]], [2,5]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    ]

NN = createInput()
for N in NN:
    print("===================")
    print(N)
    print(insert(N[0],N[1]))
    print("===================")
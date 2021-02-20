#In the end this equation worked all because of an elif used instead of if
#lesson learned that an elif meaning else if can not substitute and if
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pairs = [0,1,arrayOne[0],arrayTwo[0]]
    for value in arrayOne:
        left = 0
        pairs[0],pairs[1]= value,arrayTwo[left]
        distance = abs(value-arrayTwo[left])
        for i in range(len(arrayTwo)):
            if distance > abs(value - arrayTwo[left]):
                pairs[0],pairs[1] = value,arrayTwo[left]
                distance = abs(pairs[0] - pairs[1])
            if abs(pairs[0]-pairs[1]) < abs(pairs[2]-pairs[3]):
                pairs[2],pairs[3] = pairs[0],pairs[1]
            left+=1
    return [pairs[2],pairs[3]]
array1 = [-1,5,10,20,28,3]
array2 = [26,134,135,15,17]
arrayO = [10, 0, 20, 25, 2200]
arrayT = [1005, 1006, 1014, 1032, 1031]
smallestDifference(arrayO,arrayT)
light = [0,1]
jay = 20
jam = 43
light[0],light[1] = jay,jam
print(light)
for i in light:
     print(i)
print(arrayT[-1])
print(arrayT[0:2])

def small(array1, array2):
    array1.sort()
    array2.sort()
    pairs = [0,1,array1[0],array2[0]]
    print("first pairs 2 and 3",array1[0],array2[0])
    for value in array1:
        left = 0
        pairs[0],pairs[1]= value,array2[left]
        print("value",value,"pairs 0 and 1",pairs[0],pairs[1])
        distance = abs(value-array2[left])
        print('distance',distance)
        for i in range(len(array2)):
            print("value again", value, "array2 left increase", array2[left])
            print("abs",abs(value-array2[left]))
            print("distance again",distance)
            if distance > abs(value - array2[left]):
                pairs[0],pairs[1] = value,array2[left]
                distance = abs(pairs[0] - pairs[1])
                print("another distance",distance)
                print("new Pairs",pairs[0],pairs[1])
                print("2 and 3 pairs", pairs[2], pairs[3])
            if abs(pairs[0]-pairs[1]) < abs(pairs[2]-pairs[3]):
                pairs[2],pairs[3] = pairs[0],pairs[1]
                print("changing pairs 2 and 3", pairs[2],pairs[3])
            left+=1
    return [pairs[2],pairs[3]]
small(arraye,arrayo)
arraye = [0, 20]
arrayo=[21, -2]

#Below is the solution from video explanation
# time complexity = O(nLog(n) + mLog(m))
# n is the lengths of array1 and m is the length of array2
def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        current = abs(firstNum-secondNum)
        if firstNum < secondNum:
            #current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            #current = firstNum - secondNum
            idxTwo +=1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
smallestDifference(array1,array2)

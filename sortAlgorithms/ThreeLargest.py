def threeLargest(array):
    newArray = [None, None, None]
    for num in array:
        updateArray(newArray, num)
    return newArray

 def updateArray(threeLargest,num):
     if threeLargest[2] is None or num > threeLargest[2]:
         shiftAndUpdate(threeLargest, num, 2)
     elif threeLargest[1] is None or num > threeLargest[1]:
         shiftAndUpdate(threeLargest, num, 1)
     elif threeLargest[0] is None or num > threeLargest[0]:
         shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]


tester = [18, 4, 5, 17, 22]
threeLargest(tester)


def First(array):
    largest = [None, None, None]
    for num in array:
        updating(largest, num)
    return threeLargest

def updating(largest, num):
    if largest[2] is None or num > largest[2]:
        shifting(largest, num, 2)
    elif largest[1] is None or num > largest[1]:
        shifting(largest, num, 1)
    elif largest[0] is None or num:
        shifting(largest, num, 0)
def shifting(array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

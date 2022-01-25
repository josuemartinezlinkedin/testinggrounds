def moveElementToEnd(array,ToMove):
    a2 = []
    for i in array:
        if i == ToMove:
            a2.append(i)
    for i in a2:
        array.remove(i)
    last = array + a2
    array = []
    a2 = []
    return last
    b = [i for  i in range(15)]
    b = b + [2,2,2,2]
    moveElementToEnd(b,2)
    

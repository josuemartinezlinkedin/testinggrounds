def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(sequence) < 1:
        return null
    elif len(sequence) <= len(array):
        if len(sequence)==len(array):
            for i in range(len(sequence)):
                if sequence[i] == array[i]:
                    continue
                elif sequence[i] != array[i]:
                    return False
            return True
        else:
            array.sort()
            sequence.sort()
            counter = 0
            for i in range(len(sequence)):
                if sequence[i] in array:
                    array.remove(sequence[i])
                    counter +=1
                    if counter == len(sequence):
                        return True
                    continue
                if sequence[i] not in array:
                    return False
    else:
        return False
array = [1,1,6,1]
sequence = [1,1,1,6]
array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [5, 1, 22, 25, 6, -1, 8, 10]
array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [1,6,-1,-1,10]
sequence4 = [1,6,-1,10]
array5 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence5 = [5, 1, 25, 22, 6, -1, 8, 10]

isValidSubsequence(array5,sequence5)

#Just in case I forgot any changes here
#here is the code again that passed
"""
def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(sequence) < 1:
        return null
    elif len(sequence) <= len(array):
        if len(sequence)==len(array):
            for i in range(len(sequence)):
                if sequence[i] == array[i]:
                    continue
                elif sequence[i] != array[i]:
                    return False
            return True
        else:
			array.sort()
			sequence.sort()
            counter = 0
            for i in range(len(sequence)):
                if sequence[i] in array:
                    array.remove(sequence[i])
                    counter +=1
                    if counter == len(sequence):
                        return True
                    continue
                if sequence[i] not in array:
                    return False
    else:
        return False
"""

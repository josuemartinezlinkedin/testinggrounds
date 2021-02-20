def four_sum(array,targetSum):
    quadruplets = []
    numberPairs = {}
    for i in range(1, len(array)-1): #here we are skipping first iteration
        for j in range(i+1,len(array)): #goes to end of array starting from i +1
            currentSum = array[i]+array[j]
            difference = targetSum - currentSum
            if difference in numberPairs:
                for pair in numberPairs[difference]:#for stored pairs add new pairs
                #look below for sample code 1
                    quadruplets.append(pair+[array[i], array[j]])
        for k in range(0,i):
            currentSum = array[k]+array[i]
            if currentSum not in numberPairs:
                numberPairs[currentSum] = [ [array[k], array[i]] ]
            else:
                numberPairs[currentSum].append([array[k],array[i]])
    return quadruplets


# sample code 1
some = {10:[9,1], 12:[[11,1],[10,2]]}
some[10].append([8,7])
some[10]
for i in some[12]:
    print(i)
#[11,1]
#[10,2]

secondlist = [7,6,4,-1,1,2]
four_sum(secondlist,16)


sums = {}
ar = []
sums[20] = [ [ar[k], ar[i]] ]


def again(targetSum, array):
    quads = []
    mypairs = {}
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in mypairs:
                for pair in mypairs[difference]:
                    quads.append(pair+[array[i], array[k]])

    return quads

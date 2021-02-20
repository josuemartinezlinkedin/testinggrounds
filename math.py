listone = [1,4,9,10,2,7,5,3,6,2,2,1,7]

def hmm(listone,target):
    newlist = []
    firstdic = {}
    for i in listone:
        l = i
    for j in range(len(listone)):
        if (target - l) in firstdic:
            if [i,target-l] not in newlist:
                newlist.append([i,target-i])
                return [listone.index(i),j]
            elif (target - i) in listone:
                firstdic[i] = i - target

hmm([3,3],6)



#create a empty hash
#if a number is in the hash then that means that it's pair is in
#if the number is not in the list see why
#means take it and add it to the list but only if it minus target is in list

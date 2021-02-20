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

function smallestDifference(array1,array2){
array1.sort();
array2.sort();
var ind1 = 0;
var ind2 = 0;
smallest = Infinity;
current = Infinity;
const smallestPair = []
while (in1< array1.length AND array2.length){
  firstNum = array1[ind1]
  secondNum = array2[ind2]
  current = Math.abs(firstNum-secondNum)
  if (firstNum<secondNum){
    ind1 +=1
  } else if (secondNum < firstNum){
    ind1 += 1
  } else {
    return [firstNum, secondNum]
  } if (smallest > current){
    smallest = current
    smallestPair = [firstNum, secondNum]
  }
}
return smallestPair
};

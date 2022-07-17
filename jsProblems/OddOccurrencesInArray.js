/*
1st solution using XOR operator which is the fastest method

like turning switches on and off, and when a pattern has already been displyed
then leaves just the unique binary pattern
a = 1  //001
b = 2 //010
 a ^ b = 3 // 011
*/
function solution1 (A) {
    result = 0
    for (let element of A ) {
        result = result ^ element
    }
    return result;
}

//second solution more readable but sorting first then traversing array can be costly
function solution2(A) {
    A.sort()
    if (A.length < 2) { return A[0] }
    else {
        for (i = 0; i < A.length; i++) {
            if (A[i] !== A[i + 1] && A[i] !== A[i - 1]) {
                return A[i]
            }
        }
    }
}

//another vaiation with else statement removed
function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    A.sort()
    if (A.length < 2) { return A[0] }
    let i = 0
    for (let element of A) {
        if (A[i] !== A[i + 1] && A[i] !== A[i - 1]) {
            return A[i]
        }
        i++
    }
}
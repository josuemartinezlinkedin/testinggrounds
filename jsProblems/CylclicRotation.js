//takes array of numbers as A and an integer value as K
function solution(A,K) {
    
    if (A.length < 2) {
        return A
    }
    
    for (i=0; i<K; i++) {
        valueToFront = A.pop()
        A.unshift(valueToFront)
    }
    return A
}
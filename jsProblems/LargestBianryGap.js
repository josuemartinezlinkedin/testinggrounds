function solution(N) {    
    if (N < 5) {
        return 0
    } if (N === 5) { return 1 }
    else {
        const binaryN = N.toString(2)
        let greatest = 0
        let tracking = 0
        for (i = 1; i < binaryN.length; i++) {
            if (binaryN[i] === '0') {
                tracking++
            }
            if (binaryN[i] === '1') {
                if (tracking > greatest) {
                    greatest = tracking
                }
                tracking = 0
            }
        } return greatest
    }
}
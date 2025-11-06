/**
 * @param {number} n
 * @return {number}
 */
var smallestNumber = function(n) {

    let count = 0
    let temp = n

    while (temp > 0) {
        count += temp & 1;
        temp >>= 1;
    }
    
    let result = (1 << count) -1
    
    while (result < n) {
        count ++;
        result = (1 << count) -1;
    }

    return result

};

console.log(smallestNumber(5))
console.log(smallestNumber(10))
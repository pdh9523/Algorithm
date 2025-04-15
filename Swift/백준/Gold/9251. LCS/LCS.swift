import Foundation


let a = readLine()!
let b = readLine()!

let aLength = a.count
let bLength = b.count

let aChars = Array(a)
let bChars = Array(b)

var DP = [Int](repeating: 0, count: bLength)

for i in 0..<aLength {
    var cnt = 0
    for j in 0..<bLength {
        if cnt < DP[j] {
            cnt = DP[j]
        } else if aChars[i] == bChars[j] {
            DP[j] = cnt + 1
        }
    }
}

print(DP.max()!)
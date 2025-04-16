import Foundation


func check(_ arr: [Int],_ target: Int) -> Bool {
    var (group, totalScore) = (0,0)
    for score in arr {
        totalScore += score
        if totalScore >= target {
            group += 1
            totalScore = 0
        }
    }
    return group >= K
}

let input = readLine()!.split(separator: " ").compactMap { Int($0) }
let (N,K) = (input[0], input[1])
let arr = readLine()!.split(separator: " ").compactMap { Int($0) }

var (left,right) = (0, 2*Int(pow(10.0, 6.0)))
while left <= right {
    let mid = (left+right) / 2

    if check(arr, mid) {
        left = mid + 1
    } else {
        right = mid - 1
    }
}

print(right)
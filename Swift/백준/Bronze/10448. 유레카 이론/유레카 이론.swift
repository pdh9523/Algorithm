import Foundation


var tmp: [Int] = []
for i in 1..<45 {
    tmp.append(i*(i+1) / 2)
}

var res = [Int](repeating: 0, count: 1001)
for a in tmp {
    for b in tmp {
        for c in tmp {
            if a+b+c <= 1000 {
                res[a+b+c] = 1
            }
        }
    }
}

let N = Int(readLine()!)!
for _ in 0..<N {
    print(res[Int(readLine()!)!])
}
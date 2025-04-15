import Foundation


let group = readLine()!
let password = readLine()!
let length = group.count

var data : [Character: Int] = [:]
for (i,ch) in group.enumerated() {
    data[ch] = i+1
}

var ans = 0

for ch in password {
    ans *= length

    if let value = data[ch] {
        ans += value
    }
    ans %= 900528
}

print(ans)
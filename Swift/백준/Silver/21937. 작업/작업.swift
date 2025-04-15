import Foundation


struct Deque<T> {
    private var left: [T] = []
    private var right: [T] = []

    var isEmpty: Bool {
        return left.isEmpty && right.isEmpty
    }

    mutating func popleft() -> T? {
        if left.isEmpty {
            left = right.reversed()
            right.removeAll()
        }
        return left.popLast()
    }

    mutating func append(_ x: T) {
        right.append(x)
    }
}


var input = readLine()!.split(separator: " ").compactMap{Int($0)}
let (N,M) = (input[0], input[1])

var graph = [[Int]](repeating: [], count: N+1)
for _ in (0..<M) {
   input = readLine()!.split(separator: " ").compactMap{Int($0)}
   let (a,b) = (input[0], input[1])
   graph[b].append(a)
}

let start = Int(readLine()!)!
var q = Deque<Int>()
q.append(start)
var visit = [Bool](repeating: false, count: N+1)
visit[start] = true

var ans = 0 
while !q.isEmpty {
    let now = q.popleft()!

    for nxt in graph[now] {
        guard !visit[nxt] else {
            continue
        }
        ans += 1
        q.append(nxt)
        visit[nxt] = true
    }
}

print(ans)
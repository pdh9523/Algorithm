package main

import (
	"bufio"
	"container/list"
	"os"
	"strconv"
)

var (
	dx = [2]int{0, 1}
	dy = [2]int{1, 0}
)

type Node struct {
	x, y int
}

func (n Node) unpack() (int, int) {
	return n.x, n.y
}

func bfs(arr [][]bool, N, M int) bool {
	start := Node{0, 0}

	stack := list.New()
	stack.PushBack(start)
	for stack.Len() > 0 {
		x, y := stack.Remove(stack.Back()).(Node).unpack()

		if x == N-1 && y == M-1 {
			return true
		}

		for i := 0; i < 2; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if 0 <= nx && nx < N && 0 <= ny && ny < M {
				if arr[nx][ny] {
					arr[nx][ny] = false
					stack.PushBack(Node{nx, ny})
				}
			}
		}
	}
	return false
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	M, N := intInput(), intInput()

	arr := make([][]bool, N)
	for i := 0; i < N; i++ {
		arr[i] = make([]bool, M)
		for j := 0; j < M; j++ {
			if intInput() == 1 {
				arr[i][j] = true
			} else {
				arr[i][j] = false
			}
		}
	}
	var ans string
	if bfs(arr, N, M) {
		ans = "Yes"
	} else {
		ans = "No"
	}

	bw.WriteString(ans)
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

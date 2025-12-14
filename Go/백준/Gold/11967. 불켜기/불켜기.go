package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strconv"
)

var (
	dx = [4]int{0, 1, 0, -1}
	dy = [4]int{1, 0, -1, 0}
)

type Node struct {
	x, y int
}

func (n Node) unpack() (int, int) {
	return n.x, n.y
}

func check(visit [][]bool, x, y int) bool {
	for i := 0; i < 4; i++ {
		nx, ny := x+dx[i], y+dy[i]
		if 0 <= nx && nx < len(visit) && 0 <= ny && ny < len(visit) {
			if visit[nx][ny] {
				return true
			}
		}
	}
	return false
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := intInput(), intInput()
	arr := make([][]bool, N)
	visit := make([][]bool, N)
	for i := 0; i < N; i++ {
		arr[i] = make([]bool, N)
		visit[i] = make([]bool, N)
	}
	arr[0][0] = true
	visit[0][0] = true
	data := make(map[Node][]Node)
	for i := 0; i < M; i++ {
		x, y, a, b := intInput()-1, intInput()-1, intInput()-1, intInput()-1
		if _, exists := data[Node{x, y}]; !exists {
			data[Node{x, y}] = make([]Node, 0)
		}
		data[Node{x, y}] = append(data[Node{x, y}], Node{a, b})
	}

	q := list.New()
	q.PushBack(Node{0, 0})
	for q.Len() > 0 {
		node := q.Remove(q.Front()).(Node)
		if _, exists := data[node]; exists {
			for _, n := range data[node] {
				x, y := n.unpack()
				arr[x][y] = true
				if check(visit, x, y) {
					if !visit[x][y] {
						visit[x][y] = true
						q.PushBack(n)
					}
				}
			}
		}

		x, y := node.unpack()

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if 0 <= nx && nx < N && 0 <= ny && ny < N {
				if arr[nx][ny] && !visit[nx][ny] {
					visit[nx][ny] = true
					q.PushBack(Node{nx, ny})
				}
			}
		}
	}
	ans := 0
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if arr[i][j] {
				ans++
			}
		}
	}
	fmt.Fprintln(bw, ans)
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

package main

import (
	"bufio"
	"container/list"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	N := intInput()

	graph := make([][]int, N+1)
	for i := 1; i < N+1; i++ {
		graph[i] = make([]int, 0)
	}

	for i := 1; i < N+1; i++ {
		x := intInput()
		graph[x] = append(graph[x], i)
	}

	visit := make([]int, N+1)
	visit[N] = 1

	q := list.New()
	q.PushBack(N)

	for q.Len() > 0 {
		now := q.Remove(q.Front()).(int)

		for _, next := range graph[now] {
			if visit[next] == 0 {
				visit[next] = visit[now] + 1
				q.PushBack(next)
			}
		}
	}

	for i := 1; i < N+1; i++ {
		bw.WriteString(strconv.Itoa(visit[i]-1) + "\n")
	}
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

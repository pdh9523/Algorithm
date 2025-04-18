package main

import (
	"bufio"
	"container/list"
	"os"
	"sort"
	"strconv"
)

type Node struct {
	x, y int
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M, R := input(), input(), input()

	arr := make([]Node, M)
	for i := 0; i < M; i++ {
		arr[i] = Node{input(), input()}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].x == arr[j].x {
			return arr[i].y < arr[j].y
		} else {
			return arr[i].x < arr[j].x
		}
	})
	graph := make([][]int, N+1)
	for i := 1; i < N+1; i++ {
		graph[i] = make([]int, 0)
	}
	for _, node := range arr {
		graph[node.x] = append(graph[node.x], node.y)
		graph[node.y] = append(graph[node.y], node.x)
	}
	visit := make([]int, N+1)
	visit[R] = 1
	q := list.New()
	q.PushBack(R)
	cnt := 1
	for q.Len() > 0 {
		now := q.Remove(q.Front()).(int)
		for _, next := range graph[now] {
			if visit[next] == 0 {
				q.PushBack(next)
				cnt++
				visit[next] = cnt
			}
		}
	}
	for i := 1; i < N+1; i++ {
		bw.WriteString(strconv.Itoa(visit[i]) + "\n")
	}
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}

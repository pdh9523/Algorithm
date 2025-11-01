package main

import (
	"bufio"
	"container/heap"
	"os"
	"strconv"
)

type Pos struct {
	x, y int
}

type Node struct {
	idx, value int
}

func (n Node) unpack() (int, int) {
	return n.idx, n.value
}

type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i].value < h[j].value
}

func (h HeapQ) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *HeapQ) Push(x interface{}) {
	*h = append(*h, x.(Node))
}

func (h *HeapQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func getDist(a, b Pos) int {
	return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, C := input(), input()
	points := make([]Pos, N)
	for i := 0; i < N; i++ {
		points[i] = Pos{input(), input()}
	}

	graph := make([][]Node, N)
	for i := 0; i < N; i++ {
		graph[i] = make([]Node, 0)
	}
	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			dist := getDist(points[i], points[j])
			if dist >= C {
				graph[i] = append(graph[i], Node{j, dist})
				graph[j] = append(graph[j], Node{i, dist})
			}
		}
	}
	ans := 0
	hq := &HeapQ{}
	heap.Init(hq)
	heap.Push(hq, Node{0, 0})
	visit := make([]bool, N)
	for hq.Len() > 0 {
		now, cost := heap.Pop(hq).(Node).unpack()

		if !visit[now] {
			visit[now] = true
			ans += cost
			for _, nxt := range graph[now] {
				heap.Push(hq, nxt)
			}
		}
	}
	for i := 0; i < N; i++ {
		if !visit[i] {
			bw.WriteString("-1")
			return
		}
	}
	bw.WriteString(strconv.Itoa(ans))
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

package main

import (
	"bufio"
	"container/heap"
	"os"
	"strconv"
)

type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i].x < h[j].x
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

type Node struct {
	x, y int
}

func (n Node) unpack() (int, int) {
	return n.x, n.y
}

func mst(size int, graph [][]Node) int {
	visit := make([]bool, size+1)
	hq := &HeapQ{}
	heap.Init(hq)
	heap.Push(hq, Node{0, 0})
	res := 0
	for hq.Len() > 0 {
		dist, now := heap.Pop(hq).(Node).unpack()
		if visit[now] {
			continue
		}
		visit[now] = true
		res += dist
		for _, next := range graph[now] {
			heap.Push(hq, next)
		}
	}
	return res
}

func square(num int) int {
	return num * num
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	maxGraph := make([][]Node, N+1)
	minGraph := make([][]Node, N+1)
	for i := 0; i < N+1; i++ {
		maxGraph[i] = make([]Node, 0)
		minGraph[i] = make([]Node, 0)
	}
	for i := 0; i < M+1; i++ {
		a, b, c := input(), input(), input()
		maxGraph[a] = append(maxGraph[a], Node{c, b})
		maxGraph[b] = append(maxGraph[b], Node{c, a})
		minGraph[a] = append(minGraph[a], Node{1 - c, b})
		minGraph[b] = append(minGraph[b], Node{1 - c, a})
	}

	maxValue := square(N - mst(N, maxGraph))
	minValue := square(mst(N, minGraph))
	bw.WriteString(strconv.Itoa(maxValue - minValue))
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

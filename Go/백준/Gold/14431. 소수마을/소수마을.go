package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt

type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i].cost < h[j].cost
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
	*h = old[0 : n-1]
	return x
}

type Node struct {
	idx  int
	cost int
}

func (n Node) unpack() (int, int) {
	return n.idx, n.cost
}

type Point struct {
	x, y int
}

func newPoint(x, y int) Point {
	return Point{x, y}
}

func getDistance(a, b Point) int {
	return int(math.Sqrt((math.Pow(float64(a.x-b.x), 2) + math.Pow(float64(a.y-b.y), 2))))
}

func getPrimes() map[int]bool {
	// getDistance((-3000,-3000), (3000,3000)) ~= 8485
	size := 8490

	isNotPrime := make([]bool, size+1)
	for i := 2; i < size+1; i++ {
		if !isNotPrime[i] {
			for j := i + i; j < size+1; j += i {
				isNotPrime[j] = true
			}
		}
	}

	res := make(map[int]bool)
	for i := 2; i < size+1; i++ {
		if !isNotPrime[i] {
			res[i] = true
		}
	}
	return res
}

func dijkstra(size int, graph [][]Node) int {
	hq := &HeapQ{}
	heap.Init(hq)
	heap.Push(hq, Node{0, 0})

	distance := make([]int, size)
	for i := 0; i < size; i++ {
		distance[i] = MAX_VALUE
	}
	distance[0] = 0

	for hq.Len() > 0 {
		now, distNow := heap.Pop(hq).(Node).unpack()

		if distNow > distance[now] {
			continue
		}

		for _, nxt := range graph[now] {
			idxNxt, costNxt := nxt.unpack()
			if distance[idxNxt] > distNow+costNxt {
				distance[idxNxt] = distNow + costNxt
				heap.Push(hq, Node{idxNxt, distance[idxNxt]})
			}
		}
	}

	if distance[1] == MAX_VALUE {
		return -1
	}
	return distance[1]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	start, end := newPoint(intInput(), intInput()), newPoint(intInput(), intInput())

	N := intInput()
	points := make([]Point, N+2)
	points[0] = start
	points[1] = end
	for i := 2; i < N+2; i++ {
		points[i] = newPoint(intInput(), intInput())
	}
	primes := getPrimes()

	graph := make([][]Node, N+2)
	for i := 0; i < N+2; i++ {
		graph[i] = make([]Node, 0)
	}

	for i := 0; i < N+2; i++ {
		for j := i + 1; j < N+2; j++ {
			dist := getDistance(points[i], points[j])
			if _, exists := primes[dist]; exists {
				graph[i] = append(graph[i], Node{j, dist})
				graph[j] = append(graph[j], Node{i, dist})
			}
		}
	}
	fmt.Fprintln(bw, dijkstra(N+2, graph))
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

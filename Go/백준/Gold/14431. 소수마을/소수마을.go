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
	dx := a.x - b.x
	dy := a.y - b.y
	return int(math.Sqrt(float64(dx*dx + dy*dy)))
}

func getPrimes() []bool {
	// getDistance((-3000,-3000), (3000,3000)) ~= 8485
	size := 8490

	isNotPrime := make([]bool, size+1)
	isNotPrime[0] = true
	isNotPrime[1] = true
	for i := 2; i < size+1; i++ {
		if !isNotPrime[i] {
			for j := i * i; j < size+1; j += i {
				isNotPrime[j] = true
			}
		}
	}
	return isNotPrime
}

func dijkstra(size int, points []Point, notPrimes []bool) int {
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

		for nxt, point := range points {
			cost := getDistance(points[now], point)
			if !notPrimes[cost] && distance[nxt] > distNow+cost {
				distance[nxt] = distNow + cost
				heap.Push(hq, Node{nxt, distance[nxt]})
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
	notPrimes := getPrimes()
	fmt.Fprintln(bw, dijkstra(N+2, points, notPrimes))
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

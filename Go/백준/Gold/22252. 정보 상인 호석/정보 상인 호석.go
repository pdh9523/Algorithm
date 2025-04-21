package main

import (
	"bufio"
	"container/heap"
	"os"
	"strconv"
)

type HeapQ []int

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h HeapQ) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *HeapQ) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *HeapQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := inputInt()

	data := make(map[string]*HeapQ)
	ans := 0
	for i := 0; i < N; i++ {
		cmd := inputInt()
		name := input()
		if cmd == 1 {
			size := inputInt()
			if _, exists := data[name]; !exists {
				data[name] = &HeapQ{}
				heap.Init(data[name])
			}
			for j := 0; j < size; j++ {
				heap.Push(data[name], inputInt())
			}
		} else {
			cnt := inputInt()
			if _, exists := data[name]; !exists {
				continue
			}
			cnt = min(cnt, data[name].Len())
			for j := 0; j < cnt; j++ {
				ans += heap.Pop(data[name]).(int)
			}
		}
	}
	bw.WriteString(strconv.Itoa(ans))
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func inputInt() int {
	num, _ := strconv.Atoi(input())
	return num
}

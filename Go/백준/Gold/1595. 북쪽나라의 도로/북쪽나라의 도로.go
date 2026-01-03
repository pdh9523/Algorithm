package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strconv"
)

type Node struct {
	idx    int
	weight int
}

func (n Node) unpack() (int, int) {
	return n.idx, n.weight
}

func dfs(start int, graph [][]Node) (int, int) {
	stack := list.New()
	stack.PushBack(Node{start, 0})

	visit := make([]bool, 10001)

	ans := 0
	ansWeight := 0

	for stack.Len() > 0 {
		now, nowWeight := stack.Remove(stack.Back()).(Node).unpack()

		if visit[now] {
			continue
		}

		if ansWeight < nowWeight {
			ans = now
			ansWeight = nowWeight
		}

		visit[now] = true

		for _, nxt := range graph[now] {
			nxtIdx, nxtWeight := nxt.unpack()
			stack.PushBack(Node{nxtIdx, nowWeight + nxtWeight})
		}
	}
	return ans, ansWeight
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	graph := make([][]Node, 10001)
	for i := 0; i < 10001; i++ {
		graph[i] = make([]Node, 0)
	}
	var start int = 0
	for {
		node, exists := input()
		if !exists {
			break
		}
		a, b, c := node[0], node[1], node[2]

		graph[a] = append(graph[a], Node{b, c})
		graph[b] = append(graph[b], Node{a, c})
		start = a
	}

	idx, _ := dfs(start, graph)
	_, ans := dfs(idx, graph)
	fmt.Fprintln(bw, ans)
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() ([]int, bool) {
	input := make([]int, 3, 3)
	for i := 0; i < 3; i++ {
		if !bs.Scan() {
			return input, false
		}
		input[i] = atoi(bs.Text())
	}
	return input, true
}

func atoi(s string) int {
	num, _ := strconv.Atoi(s)
	return num
}

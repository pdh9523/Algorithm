package main

import (
	"bufio"
	"os"
	"strconv"
)

type Node struct {
	idx, cost int
}

func (n Node) unpack() (int, int) {
	return n.idx, n.cost
}

func dfs(tree [][]Node, prev int, now int) int {
	res := 0
	for _, node := range tree[now] {
		nxt, cost := node.unpack()
		if nxt != prev {
			res += min(cost, dfs(tree, now, nxt))
		}
	}
	if res == 0 {
		return 1e9
	}
	return res
}

func solve() {
	N, M := intInput(), intInput()
	if N == 1 {
		bw.WriteString("0")
		return
	}
	tree := make([][]Node, N+1)
	for i := 1; i < N+1; i++ {
		tree[i] = make([]Node, 0)
	}
	for i := 0; i < M; i++ {
		a, b, c := intInput(), intInput(), intInput()
		tree[a] = append(tree[a], Node{b, c})
		tree[b] = append(tree[b], Node{a, c})
	}

	bw.WriteString(strconv.Itoa(dfs(tree, 1, 1)))
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	tc := intInput()
	for t := 0; t < tc; t++ {
		solve()
		bw.WriteString("\n")
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

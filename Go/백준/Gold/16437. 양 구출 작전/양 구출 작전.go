package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Node struct {
	typ    string
	amount int
}

func (n Node) unpack() (bool, int) {
	return n.typ == "W", n.amount
}

func dfs(arr []Node, tree [][]int, now int) int {
	res := 0

	for _, nxt := range tree[now] {
		res += dfs(arr, tree, nxt)
	}

	isWolf, amount := arr[now].unpack()

	if isWolf {
		res -= amount
		if res < 0 {
			res = 0
		}
	} else {
		res += amount
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()

	tree := make([][]int, N+1)
	for i := 1; i < N+1; i++ {
		tree[i] = make([]int, 0)
	}
	arr := make([]Node, N+2)

	for i := 2; i < N+1; i++ {
		a, b, c := input(), intInput(), intInput()
		arr[i] = Node{a, b}
		tree[c] = append(tree[c], i)
	}

	fmt.Fprintln(bw, dfs(arr, tree, 1))
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

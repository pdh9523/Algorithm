package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	tree   [][]int
	values []int
)

func dfs(now int) int {
	if len(tree[now]) == 0 {
		return values[now]
	}

	res := 0
	for _, nxt := range tree[now] {
		tmp := dfs(nxt)
		if tmp > 0 {
			res += tmp
		}
	}
	return res + values[now]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()

	tree = make([][]int, N)
	for i := 0; i < N; i++ {
		tree[i] = make([]int, 0)
	}

	for i := 0; i < N-1; i++ {
		a, b := input(), input()
		tree[a] = append(tree[a], b)
	}
	values = make([]int, N)
	for i := 0; i < N; i++ {
		values[i] = input()
	}

	bw.WriteString(strconv.Itoa(dfs(0)))
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

package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	cnt   = 0
	visit []bool
)

func dfs(graph [][]int, now int, depth int) {
	if visit[now] {
		return
	}

	visit[now] = true
	if len(graph[now]) == 1 {
		cnt += depth
	}
	for _, nxt := range graph[now] {
		dfs(graph, nxt, depth+1)
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()

	visit = make([]bool, N+1)

	graph := make([][]int, N+1)
	for i := 1; i < N+1; i++ {
		graph[i] = make([]int, 0)
	}

	for i := 0; i < N-1; i++ {
		a, b := intInput(), intInput()
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}

	dfs(graph, 1, 0)

	ans := "Yes"
	if cnt%2 == 0 {
		ans = "No"
	}

	bw.WriteString(ans)
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

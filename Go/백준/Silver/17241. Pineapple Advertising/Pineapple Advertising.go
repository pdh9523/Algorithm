package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M, Q := input(), input(), input()
	graph := make([][]int, N+1)
	for i := range graph {
		graph[i] = make([]int, 0)
	}
	for i := 0; i < M; i++ {
		a, b := input(), input()
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	visit := make([]bool, N+1)
	cache := make([]bool, N+1)
	for i := 0; i < Q; i++ {
		now := input()
		cnt := 0
		if cache[now] {
			bw.WriteString("0\n")
			continue
		}
		cache[now] = true
		if !visit[now] {
			cnt++
			visit[now] = true
		}

		for _, next := range graph[now] {
			if !visit[next] {
				cnt++
				visit[next] = true
			}
		}
		bw.WriteString(strconv.Itoa(cnt) + "\n")
	}
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

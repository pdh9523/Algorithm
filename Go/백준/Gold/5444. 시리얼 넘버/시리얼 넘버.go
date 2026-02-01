package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve() {
	N, M := intInput(), intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}
	now := make([]int, M)
	nxt := make([]int, M)
	for i := 0; i < M; i++ {
		now[i] = -1
		nxt[i] = -1
	}
	now[0] = 0

	for _, v := range arr {
		for i := 0; i < M; i++ {
			if now[i] < 0 {
				continue
			}
			nxtValue := (i + v) % M
			nxt[nxtValue] = max(nxt[nxtValue], now[i]+1)
		}
		for i := 0; i < M; i++ {
			now[i] = nxt[i]
		}
	}
	fmt.Fprintln(bw, now[0])
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	T := intInput()
	for i := 0; i < T; i++ {
		solve()
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

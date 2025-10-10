package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	dist := make([]int, N-1)
	for i := 0; i < N-1; i++ {
		dist[i] = input()
	}
	cost := make([]int, N)
	for i := 0; i < N; i++ {
		cost[i] = input()
	}

	nowDist := 0
	nowCost := MAX_VALUE
	ans := 0
	for i := 0; i < N-1; i++ {
		if nowCost > cost[i] {
			ans += nowDist * nowCost
			nowCost = cost[i]
			nowDist = 0
		}
		nowDist += dist[i]
	}
	ans += nowDist * nowCost
	bw.WriteString(strconv.Itoa(ans))
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

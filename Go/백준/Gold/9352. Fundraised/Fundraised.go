package main

import (
	"bufio"
	"os"
	"strconv"
)

func max(args ...int) int {
	res := 0
	for _, a := range args {
		if res < a {
			res = a
		}
	}
	return res
}

func solve() {
	N, X := intInput(), intInput()

	value := make([]int, N)
	for i := 0; i < N; i++ {
		value[i] = intInput()
	}

	cost := make([]int, N)
	for i := 0; i < N; i++ {
		cost[i] = intInput()
	}

	DP := make([]int, X+1)
	for i := 0; i < N; i++ {
		c := cost[i]
		v := value[i]
		for a := c; a <= X; a++ {
			DP[a] = max(DP[a], DP[a-c]+v)
		}
	}
	bw.WriteString(strconv.Itoa(DP[X]) + "\n")
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	tc := intInput()
	for t := 0; t < tc; t++ {
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

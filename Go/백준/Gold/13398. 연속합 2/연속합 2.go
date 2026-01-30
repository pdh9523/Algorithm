package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func max(args ...int) int {
	res := -math.MaxInt
	for _, arg := range args {
		if res < arg {
			res = arg
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}

	DP := make([][]int, 2)
	for i := 0; i < 2; i++ {
		DP[i] = make([]int, N)
	}

	DP[0][0] = arr[0]
	DP[1][0] = -1000
	for i := 1; i < N; i++ {
		DP[0][i] = max(DP[0][i-1]+arr[i], arr[i])
		DP[1][i] = max(DP[0][i-1], DP[1][i-1]+arr[i])
	}

	fmt.Fprintln(bw, max(max(DP[0]...), max(DP[1]...)))
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

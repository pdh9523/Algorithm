package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(args ...int) int {
	res := 0
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

	DP := make([]int, N)

	for i, v := range arr {
		DP[i] = max(DP[i], v)
		for idx := 0; idx < i; idx++ {
			if v < arr[idx] {
				DP[i] = max(DP[i], DP[idx]+v)
			}
		}
	}
	fmt.Println(max(DP...))
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

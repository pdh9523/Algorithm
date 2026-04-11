package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	N := intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}
	ans := 1
	now := arr[N-1]
	for i := N - 2; i >= 0; i-- {
		if arr[i] > now {
			now = arr[i]
			ans++
		}
	}
	fmt.Fprintln(bw, ans)
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

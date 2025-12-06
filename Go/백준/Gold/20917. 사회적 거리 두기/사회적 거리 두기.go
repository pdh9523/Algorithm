package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

func check(diff int, cnt int, arr []int) bool {
	now := arr[0]
	c := 1
	for i := 1; i < len(arr); i++ {
		if now+diff <= arr[i] {
			c++
			now = arr[i]
		}
	}
	return c >= cnt
}

func binSearch(cnt int, arr []int) int {
	left, right := 0, 1_000_000_000
	for left < right {
		mid := (left + right + 1) / 2
		if check(mid, cnt, arr) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}

func solve() {
	N, S := intInput(), intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}
	sort.Ints(arr)
	res := binSearch(S, arr)
	bw.WriteString(strconv.Itoa(res) + "\n")
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

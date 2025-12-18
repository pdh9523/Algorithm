package main

import (
	"bufio"
	"os"
	"sort"
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

	N, K := intInput(), intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}
	sort.Ints(arr)

	sizes := make(map[int]int)
	for i := 0; i < N; i++ {
		sizes[intInput()]++
	}
	for i := 0; i < K; i++ {
		sizes[intInput()]--
	}
	size := 0
	for k, v := range sizes {
		if v == 0 {
			continue
		}
		size = max(size, k)
	}

	left := 0
	right := N - 1
	mid := 0
	for left < right {
		mid = (left + right + 1) / 2

		if arr[mid] <= size {
			left = mid
		} else {
			right = mid - 1
		}
	}
	bw.WriteString(strconv.Itoa(arr[left]))
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

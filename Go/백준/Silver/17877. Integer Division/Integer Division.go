package main

import (
	"bufio"
	"os"
	"strconv"
)

func comb(n int) int {
	res := 1
	for i := n; i > n-2; i-- {
		res *= i
	}
	for i := 2; i > 0; i-- {
		res /= i
	}

	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, D := intInput(), intInput()

	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}

	data := make(map[int]int)
	for _, a := range arr {
		x := a / D
		if _, exists := data[x]; !exists {
			data[x] = 0
		}
		data[x]++
	}
	ans := 0
	for _, x := range data {
		ans += comb(x)
	}
	bw.WriteString(strconv.Itoa(ans))
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

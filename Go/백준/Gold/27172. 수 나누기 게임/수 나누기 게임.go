package main

import (
	"bufio"
	"os"
	"strconv"
)

const SIZE = 1000000

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	arr := make([]int, N)
	check := make([]bool, SIZE+1)
	ans := make([]int, SIZE+1)

	for i := 0; i < N; i++ {
		arr[i] = intInput()
		check[arr[i]] = true
	}

	for i := 2; i*2 <= SIZE; i++ {
		if !check[i] {
			continue
		}
		for j := 2; j*i <= SIZE; j++ {
			if check[j*i] {
				ans[i]++
				ans[j*i]--
			}
		}
	}

	ans[1] = N
	for _, a := range arr {
		if check[1] {
			ans[a]--
		}
		bw.WriteString(strconv.Itoa(ans[a]) + " ")
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

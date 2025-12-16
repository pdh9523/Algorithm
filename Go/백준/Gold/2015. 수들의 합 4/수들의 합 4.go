package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, K := intInput(), intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}

	prefixSum := make([]int, N+1)
	data := make(map[int]int)
	ans := 0
	for i := 1; i < N+1; i++ {
		prefixSum[i] = prefixSum[i-1] + arr[i-1]

		if prefixSum[i] == K {
			ans++
		}
		ans += data[prefixSum[i]-K]

		data[prefixSum[i]]++

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

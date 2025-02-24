package main

import (
	"bufio"
	"os"
	"strconv"
)

type Cost struct {
	cash, card, IC int
}

func makePrefixSum(arr []int, N int) []int {
	prefixSum := make([]int, N+1)
	s := arr[0]
	for i := 1; i < len(arr); i++ {
		e := arr[i]
		if s > e {
			s, e = e, s
		}
		prefixSum[s]++
		prefixSum[e]--

		s = arr[i]
	}

	for i := 0; i < N; i++ {
		prefixSum[i+1] += prefixSum[i]
	}

	return prefixSum
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	arr := make([]int, M)
	for i := 0; i < M; i++ {
		arr[i] = input()
	}
	prefixSum := makePrefixSum(arr, N)

	costs := make([]Cost, N-1)
	for i := 0; i < N-1; i++ {
		cash, card, IC := input(), input(), input()
		costs[i] = Cost{cash, card, IC}
	}

	ans := 0
	for i := 1; i < N; i++ {
		if prefixSum[i] == 0 {
			continue
		}
		whenPayCash := prefixSum[i] * costs[i-1].cash
		whenPayCard := prefixSum[i]*costs[i-1].card + costs[i-1].IC

		ans += min(whenPayCash, whenPayCard)
	}
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

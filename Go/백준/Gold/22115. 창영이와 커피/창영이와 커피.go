package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MaxValue = math.MaxInt32

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, K := input(), input()
	DP := make([]int, K+1)
	for i := 1; i < K+1; i++ {
		DP[i] = MaxValue
	}
	coffees := make([]int, N)
	for i := 0; i < N; i++ {
		coffees[i] = input()
	}

	for _, coffee := range coffees {
		for i := K; i >= 0; i-- {
			if i+coffee > K {
				continue
			}

			DP[i+coffee] = min(DP[i+coffee], DP[i]+1)
		}
	}
	if DP[K] != MaxValue {
		bw.WriteString(strconv.Itoa(DP[K]))
	} else {
		bw.WriteString("-1")
	}
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

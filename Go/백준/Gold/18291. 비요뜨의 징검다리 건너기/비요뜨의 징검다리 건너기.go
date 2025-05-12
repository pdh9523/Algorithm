package main

import (
	"bufio"
	"os"
	"strconv"
)

const MOD = 1000000007

var DP map[int]int

func divConq(num int) int {
	if _, exists := DP[num]; exists {
		return DP[num]
	}
	if num%2 == 1 {
		DP[num] = (divConq(num/2) * divConq(num/2+1)) % MOD
	} else {
		DP[num] = (divConq(num/2) * divConq(num/2)) % MOD
	}

	return DP[num]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	DP = make(map[int]int)
	DP[1] = 2
	tc := input()
	for i := 0; i < tc; i++ {
		N := input()
		if N <= 2 {
			bw.WriteString(strconv.Itoa(1))
		} else {
			bw.WriteString(strconv.Itoa(divConq(N - 2)))
		}
		bw.WriteString("\n")
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

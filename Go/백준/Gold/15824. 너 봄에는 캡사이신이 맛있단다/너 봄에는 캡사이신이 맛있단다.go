package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const MOD = 1_000_000_007

func pow(base int, power int) int {
	switch power {
	case 1:
		return base
	case 0:
		return 1
	}

	half := pow(base, power/2)
	if power%2 == 0 {
		return half * half % MOD
	} else {
		return half * half * base % MOD
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()

	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}
	sort.Ints(arr)

	ans := 0
	for i := 0; i < N; i++ {
		ans = (ans + arr[i]*(pow(2, i)-pow(2, N-i-1))) % MOD
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

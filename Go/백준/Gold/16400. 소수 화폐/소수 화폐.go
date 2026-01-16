package main

import (
	"bufio"
	"os"
	"strconv"
)

func getPrimes(size int) map[int]bool {
	primes := make([]bool, size+1)
	res := make(map[int]bool)

	for i := 2; i < size+1; i++ {
		if !primes[i] {
			res[i] = true
			for j := i * 2; j < size+1; j += i {
				primes[j] = true
			}
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()

	DP := make([]int, N+1)
	DP[0] = 1
	primes := getPrimes(N)
	for p := range primes {
		for i := p; i < N+1; i++ {
			DP[i] = (DP[i-p] + DP[i]) % 123456789
		}
	}

	bw.WriteString(strconv.Itoa(DP[N]))
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

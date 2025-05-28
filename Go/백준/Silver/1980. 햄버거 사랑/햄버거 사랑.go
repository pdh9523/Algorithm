package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	N, M, T := input(), input(), input()
	if M < N {
		N, M = M, N
	}

	hamburger := T / N
	cola := T % N

	now := hamburger
	rem := cola

	for i := 0; i < T/N; i++ {
		now -= 1
		rem += N

		if rem >= M {
			rem -= M
			now += 1
		}

		if cola > rem {
			cola = rem
			hamburger = now
		}
	}
	bw.WriteString(fmt.Sprintf("%d %d", hamburger, cola))
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

package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt32

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func gcd(a, b int) int {
	for b > 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	D, P, Q := input(), input(), input()

	if P < Q {
		P, Q = Q, P
	}

	ans := MAX_VALUE

	for i := 0; i < min(D, lcm(P, Q))+P; i += P {
		target := max(D-i, 0)
		tmp := target / Q * Q

		if tmp < target {
			tmp += Q
		}
		if ans > tmp+i {
			ans = tmp + i
		}
	}
	bw.WriteString(strconv.Itoa(ans))
}

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}

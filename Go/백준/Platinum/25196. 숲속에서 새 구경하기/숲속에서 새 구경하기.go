package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

func max(args ...int) int {
	res := 0
	for _, arg := range args {
		if res < arg {
			res = arg
		}
	}
	return res
}

func min(args ...int) int {
	res := math.MaxInt
	for _, arg := range args {
		if res > arg {
			res = arg
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	Av, As, Ae := intInput(), intInput(), intInput()
	Bv, Bs, Be := intInput(), intInput(), intInput()
	Cv, Cs, Ce := intInput(), intInput(), intInput()

	limit := Av * Bv * Cv
	for Ae <= limit && Be <= limit && Ce <= limit {
		s := max(As, Bs, Cs)
		e := min(Ae, Be, Ce)

		if s <= e {
			bw.WriteString(strconv.Itoa(s))
			return
		}

		if Ae <= Be && Ae <= Ce {
			As += Av
			Ae += Av
		} else if Be <= Ae && Be <= Ce {
			Bs += Bv
			Be += Bv
		} else {
			Cs += Cv
			Ce += Cv
		}
	}
	bw.WriteString("-1")
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

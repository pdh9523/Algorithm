package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	if N == 0 {
		bw.WriteString("0")
		return
	}

	ans, now := 0, 0
	for i := 0; i < N; i++ {
		num := input()
		now += num
		if now > M {
			now = num
			ans++
		}
	}

	if now > 0 {
		ans++
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

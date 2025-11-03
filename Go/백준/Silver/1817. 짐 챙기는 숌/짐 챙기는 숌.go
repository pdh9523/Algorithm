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
	arr := make([]int, N)
	if N == 0 {
		bw.WriteString("0")
		return
	}

	for i := 0; i < N; i++ {
		arr[i] = input()
	}

	ans, now := 0, 0
	for _, a := range arr {
		now += a
		if now > M {
			now = a
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

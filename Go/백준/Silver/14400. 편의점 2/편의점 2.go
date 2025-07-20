package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	xPosition := make([]int, N)
	yPosition := make([]int, N)
	for i := 0; i < N; i++ {
		a, b := input(), input()
		xPosition[i] = a
		yPosition[i] = b

	}
	sort.Ints(xPosition)
	sort.Ints(yPosition)

	x, y := xPosition[N/2], yPosition[N/2]
	ans := 0
	for i := 0; i < N; i++ {
		ans += abs(x-xPosition[i]) + abs(y-yPosition[i])
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

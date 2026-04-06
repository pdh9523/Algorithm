package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer bw.Flush()
	bs.Split(bufio.ScanWords)

	A, B, C := input(), input(), input()
	T := input()

	ans := A + (max(0, (T-30-1+B)/B))*C

	fmt.Fprintln(bw, ans)
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

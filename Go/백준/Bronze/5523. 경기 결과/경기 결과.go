package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Result struct {
	left, right int
}

func (r *Result) check(a, b int) {
	if a > b {
		r.left++
	} else if a < b {
		r.right++
	}
}

func (r *Result) print() {
	fmt.Fprintf(bw, "%d %d", r.left, r.right)
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	r := Result{0, 0}
	for i := 0; i < N; i++ {
		a, b := intInput(), intInput()
		r.check(a, b)
	}
	r.print()
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

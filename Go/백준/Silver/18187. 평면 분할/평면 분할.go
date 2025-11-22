package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()

	ans := 2
	p := 2

	for N > 1 {
		ans += p
		p++
		N--
		if p%2 == 1 {
			if N != 1 {
				N--
				ans += p
			}
		}
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

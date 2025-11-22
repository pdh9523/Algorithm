package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func solve(s, p string) string {
	return strconv.Itoa(len(strings.ReplaceAll(s, p, " ")))
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	tc := intInput()
	for t := 0; t < tc; t++ {
		s, p := input(), input()
		bw.WriteString(solve(s, p) + "\n")
	}
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

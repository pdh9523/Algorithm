package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()

	for i := 1; i < N; i++ {
		bw.WriteString(strings.Repeat("*", i) + "\n")
	}

	for i := N; i > 0; i-- {
		bw.WriteString(strings.Repeat("*", i) + "\n")
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

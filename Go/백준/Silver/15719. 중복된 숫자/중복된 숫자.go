package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	bs.Buffer(buf, 100000000)
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	var sum int64 = 0

	for i := 0; i < int(N); i++ {
		sum += int64(intInput())
	}

	sum -= int64(N) * int64(N-1) / 2
	fmt.Fprintln(bw, sum)
}

var (
	bs  = bufio.NewScanner(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	buf = make([]byte, 100000000)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

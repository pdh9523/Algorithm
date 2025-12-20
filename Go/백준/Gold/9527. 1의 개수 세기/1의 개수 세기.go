package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
)

func calc(x int64) int64 {
	if x <= 0 {
		return 0
	}

	bitLen := bits.Len64(uint64(x))
	pow := int64(1) << (bitLen - 1)
	if pow == x {
		return int64(bitLen-1)*x/2 + 1
	}

	diff := x - pow
	return calc(pow) + diff + calc(diff)
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	start, end := intInput(), intInput()
	fmt.Fprintln(bw, calc(end)-calc(start-1))
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int64 {
	num, _ := strconv.ParseInt(input(), 10, 64)
	return num
}

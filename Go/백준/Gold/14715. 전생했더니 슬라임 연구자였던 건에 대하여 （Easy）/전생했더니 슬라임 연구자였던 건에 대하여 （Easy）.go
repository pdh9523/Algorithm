package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	num := intInput()
	var cnt uint

	for i := 2; i <= num; i++ {
		for num%i == 0 {
			num /= i
			cnt++
		}
		if num == 1 {
			break
		}
	}

	fmt.Fprintln(bw, bits.Len(cnt-1))
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

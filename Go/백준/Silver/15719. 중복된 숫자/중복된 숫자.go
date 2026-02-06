package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	defer bw.Flush()

	N := intInput()
	var sum int64 = 0

	for i := 0; i < N; i++ {
		sum += int64(intInput())
	}

	sum -= int64(N) * int64(N-1) / 2
	fmt.Fprintln(bw, sum)
}

var (
	br = bufio.NewReaderSize(os.Stdin, 1<<20)
	bw = bufio.NewWriter(os.Stdout)
)

func intInput() int {
	num := 0
	for {
		b, _ := br.ReadByte()
		if b >= '0' && b <= '9' {
			num = int(b - '0')
			break
		}
	}
	for {
		b, err := br.ReadByte()
		if err != nil || b < '0' || b > '9' {
			break
		}
		num = num*10 + int(b-'0')
	}
	return num
}

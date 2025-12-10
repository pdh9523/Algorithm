package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	bs.Buffer(buf, 1<<20)
	defer bw.Flush()

	N, K := intInput(), intInput()

	now := intInput()
	for i := 1; i < N; i++ {
		v := intInput()

		if now > v+K {
			bw.WriteString("NO")
			return
		}

		if v > now {
			now = v
		}
	}
	bw.WriteString("YES")
}

var (
	bs  = bufio.NewScanner(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	buf = make([]byte, 1<<20)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

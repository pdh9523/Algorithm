package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Buffer(buf, 1024*1024)
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	word := input()
	cnt := 0
	now := byte('{')
	for i := 0; i < len(word); i++ {
		if word[i] <= now {
			cnt++
		}
		now = word[i]
	}
	bw.WriteString(strconv.Itoa(cnt))
}

var (
	bs  = bufio.NewScanner(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	buf = make([]byte, 1024*1024)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

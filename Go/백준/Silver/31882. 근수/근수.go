package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func calc(num int64) int64 {
	var res int64
	res = num * (num + 1) * (num + 2) / 6
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	bs.Buffer(buf, 1024*1024)

	_ = intInput()
	word := input()
	var ans, cnt int64
	cnt = 0
	ans = 0
	for _, char := range word {
		if rune(char) == '2' {
			cnt++
		} else {
			ans += calc(cnt)
			cnt = 0
		}
	}
	ans += calc(cnt)
	fmt.Println(ans)
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

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

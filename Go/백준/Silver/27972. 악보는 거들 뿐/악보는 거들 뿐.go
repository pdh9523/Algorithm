package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	defer bw.Flush()
	bs.Split(bufio.ScanWords)

	N := input()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = input()
	}
	ans := 0
	asc := 1
	dsc := 1
	for i := 1; i < N; i++ {
		if arr[i] > arr[i-1] {
			asc++
			ans = max(ans, dsc)
			dsc = 1
		} else if arr[i] < arr[i-1] {
			dsc++
			ans = max(ans, asc)
			asc = 1
		}
	}
    
	ans = max(ans, asc, dsc)
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

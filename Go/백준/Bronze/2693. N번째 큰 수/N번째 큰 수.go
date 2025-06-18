package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	for tc := 0; tc < N; tc++ {
		arr := make([]int, 10)
		for i := 0; i < 10; i++ {
			arr[i] = input()
		}

		sort.Ints(arr)
		bw.WriteString(strconv.Itoa(arr[7]) + "\n")
	}
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

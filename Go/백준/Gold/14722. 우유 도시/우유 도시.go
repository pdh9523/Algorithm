package main

import (
	"bufio"
	"os"
	"strconv"
)

var milks = [3]int{0, 1, 2}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()

	arr := make([][]int, N)
	DP := make([][]int, N)
	for i := 0; i < N; i++ {
		DP[i] = make([]int, N)
		arr[i] = make([]int, N)
		for j := 0; j < N; j++ {
			arr[i][j] = input()
		}
	}
	if arr[0][0] == 0 {
		DP[0][0] = 1
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i > 0 {
				tmp := 0
				if DP[i-1][j]%3 == arr[i][j] {
					tmp++
				}
				DP[i][j] = max(DP[i][j], DP[i-1][j]+tmp)
			}
			if j > 0 {
				tmp := 0
				if DP[i][j-1]%3 == arr[i][j] {
					tmp++
				}
				DP[i][j] = max(DP[i][j], DP[i][j-1]+tmp)
			}
		}
	}
	bw.WriteString(strconv.Itoa(DP[N-1][N-1]))
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

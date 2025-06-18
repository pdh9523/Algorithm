package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	dx = []int{1, 0, -1, 0}
	dy = []int{0, 1, 0, -1}
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	target := input()

	arr := make([][]int, N)
	for i := 0; i < N; i++ {
		arr[i] = make([]int, N)
	}

	now := N * N
	i, j := 0, 0
	x := 0
	ans := ""
	for now > 0 {
		arr[i][j] = now
		if now == target {
			ans = fmt.Sprintf("%d %d", i+1, j+1)
		}
		now--

		if !(0 <= i+dx[x%4] && i+dx[x%4] < N && 0 <= j+dy[x%4] && j+dy[x%4] < N && arr[i+dx[x%4]][j+dy[x%4]] == 0) {
			x += 1
		}
		i += dx[x%4]
		j += dy[x%4]
	}
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			bw.WriteString(strconv.Itoa(arr[i][j]) + " ")
		}
		bw.WriteString("\n")
	}
	bw.WriteString(ans)

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

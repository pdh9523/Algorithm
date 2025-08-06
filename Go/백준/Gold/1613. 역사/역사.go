package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()

	distance := make([][]bool, N+1)
	for i := 0; i < N+1; i++ {
		distance[i] = make([]bool, N+1)
	}

	for i := 0; i < M; i++ {
		a, b := input(), input()
		distance[a][b] = true
	}

	for k := 1; k < N+1; k++ {
		for i := 1; i < N+1; i++ {
			for j := 1; j < N+1; j++ {
				distance[i][j] = distance[i][j] || (distance[i][k] && distance[k][j])
			}
		}
	}

	Q := input()
	for i := 0; i < Q; i++ {
		s, e := input(), input()
		ans := distance[s][e]
		ansReversed := distance[e][s]

		if ans {
			bw.WriteString("-1\n")
		} else if ansReversed {
			bw.WriteString("1\n")
		} else {
			bw.WriteString("0\n")
		}
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

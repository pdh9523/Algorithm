package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const MAX_VALUE = 301

type line struct {
	start, end int
}

func (l line) contains(j line) bool {
	return l.start <= j.start && j.start <= l.end
}

func min(args ...int) int {
	res := MAX_VALUE
	for _, arg := range args {
		if res > arg {
			res = arg
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	lines := make([]line, N)
	distance := make([][]int, N)
	for i := 0; i < N; i++ {
		lines[i] = line{intInput(), intInput()}
		distance[i] = make([]int, N)
		for j := 0; j < N; j++ {
			distance[i][j] = MAX_VALUE
		}
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if lines[i].contains(lines[j]) {
				distance[i][j] = 1
				distance[j][i] = 1
			}
		}
	}

	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if i == j {
					continue
				}
				distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
			}
		}
	}

	Q := intInput()
	for q := 0; q < Q; q++ {
		start, end := intInput(), intInput()
		ans := distance[start-1][end-1]
		if ans >= MAX_VALUE {
			ans = -1
		}
		fmt.Fprintln(bw, ans)
	}
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

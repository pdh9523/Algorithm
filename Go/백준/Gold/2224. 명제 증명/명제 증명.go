package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const (
	MAX_VALUE = math.MaxInt
	SIZE      = 52
)

func Btoi(b byte) int {
	if b >= 'a' {
		return int(b-'a') + 26
	}
	return int(b - 'A')
}

func Itoc(i int) string {
	if i >= 26 {
		return string('a' + i - 26)
	}
	return string('A' + i)
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	distance := make([][]int, SIZE)
	for i := 0; i < SIZE; i++ {
		distance[i] = make([]int, SIZE)
		for j := 0; j < SIZE; j++ {
			distance[i][j] = MAX_VALUE
		}
	}

	for i := 0; i < N; i++ {
		a, _, b := input(), input(), input()
		distance[Btoi(a[0])][Btoi(b[0])] = 1
	}

	for k := 0; k < SIZE; k++ {
		for i := 0; i < SIZE; i++ {
			for j := 0; j < SIZE; j++ {
				if distance[i][k] == 1 && distance[k][j] == 1 {
					distance[i][j] = 1
				}
			}
		}
	}
	ans := make([]string, 0)
	for i := 0; i < SIZE; i++ {
		for j := 0; j < SIZE; j++ {
			if i == j {
				continue
			}
			if distance[i][j] == 1 {
				ans = append(ans, fmt.Sprintf("%s => %s", Itoc(i), Itoc(j)))
			}
		}
	}
	fmt.Fprintln(bw, len(ans))
	for _, v := range ans {
		fmt.Fprintln(bw, v)
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

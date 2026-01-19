package main

import (
	"bufio"
	"os"
	"strconv"
)

const MAX_VALUE = 200001

func getDistance(distance [][]int, index int, friends []int) int {
	res := 0

	for _, friend := range friends {
		res = max(res, distance[friend][index]+distance[index][friend])
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := intInput(), intInput()

	distance := make([][]int, N+1)
	for i := 1; i < N+1; i++ {
		distance[i] = make([]int, N+1)
		for j := 1; j < N+1; j++ {
			distance[i][j] = MAX_VALUE
		}
	}

	for i := 0; i < M; i++ {
		a, b, c := intInput(), intInput(), intInput()
		distance[a][b] = c
	}

	for k := 1; k < N+1; k++ {
		for i := 1; i < N+1; i++ {
			for j := 1; j < N+1; j++ {
				if i == j {
					distance[i][j] = 0
				} else {
					distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
				}
			}
		}
	}

	friendSize := intInput()
	friends := make([]int, friendSize)
	for i := 0; i < friendSize; i++ {
		friends[i] = intInput()
	}

	ans := make([]int, 0)
	now := MAX_VALUE
	for i := 1; i < N+1; i++ {
		d := getDistance(distance, i, friends)
		if d < now {
			now = d
			ans = []int{i}
		} else if d == now {
			ans = append(ans, i)
		}
	}
	for _, a := range ans {
		bw.WriteString(strconv.Itoa(a) + " ")
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

func min(args ...int) int {
	res := MAX_VALUE
	for _, arg := range args {
		if res > arg {
			res = arg
		}
	}
	return res
}

func max(args ...int) int {
	res := 0
	for _, arg := range args {
		if res < arg {
			res = arg
		}
	}
	return res
}

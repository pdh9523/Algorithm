package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

var dr = [][2]int{
	{-1, 0},
	{1, 0},
	{0, 1},
	{0, -1},
}

func input() string {
	line, _, _ := br.ReadLine()
	return string(line)
}

type Node struct {
	x, y int
}

func main() {
	size := strings.Fields(input())
	N, _ := strconv.Atoi(size[0])
	M, _ := strconv.Atoi(size[1])

	var arr [][]bool
	var visit [][]int
	for i := 0; i < N; i++ {
		line := input()
		row := make([]bool, M)
		v := make([]int, M)
		for j, ch := range line {
			if ch == '1' {
				row[j] = true
			} else {
				row[j] = false
			}
		}
		arr = append(arr, row)
		visit = append(visit, v)
	}

	q := make([]Node, 0)
	q = append(q, Node{0, 0})
	visit[0][0] = 1

	pointer := 0
	for len(q) > 0 {
		now := q[pointer]
		pointer++
		x := now.x
		y := now.y

		if x == N-1 && y == M-1 {
			fmt.Println(visit[x][y])
			return
		}

		for i := 0; i < 4; i++ {
			nx := x + dr[i][0]
			ny := y + dr[i][1]

			if 0 <= nx && nx < N && 0 <= ny && ny < M {
				if arr[nx][ny] && visit[nx][ny] == 0 {
					q = append(q, Node{nx, ny})
					visit[nx][ny] = visit[x][y] + 1
				}
			}
		}
	}
	fmt.Println(-1)
}

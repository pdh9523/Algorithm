package main

import (
	"bufio"
	"os"
	"slices"
	"strconv"
)

const MAX_VALUE = 200000000

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

	N, R := intInput(), intInput()
	cities := make(map[string]int)
	for i := 0; i < N; i++ {
		cities[input()] = i
	}

	M := intInput()
	routes := make([]string, M)
	for i := 0; i < M; i++ {
		routes[i] = input()
	}

	distance := make([][]int, N)
	distanceWithTicket := make([][]int, N)
	for i := 0; i < N; i++ {
		distance[i] = make([]int, N)
		distanceWithTicket[i] = make([]int, N)
		for j := 0; j < N; j++ {
			distance[i][j] = MAX_VALUE
			distanceWithTicket[i][j] = MAX_VALUE
		}
	}

	K := intInput()
	for i := 0; i < K; i++ {
		t, s, e, cost := input(), input(), input(), intInput()
		cost *= 2
		sidx := cities[s]
		eidx := cities[e]
		distance[sidx][eidx] = min(distance[sidx][eidx], cost)
		distance[eidx][sidx] = min(distance[eidx][sidx], cost)
		switch {
		case slices.Contains([]string{"Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"}, t):
			distanceWithTicket[sidx][eidx] = 0
			distanceWithTicket[eidx][sidx] = 0
		case slices.Contains([]string{"S-Train", "V-Train"}, t):
			distanceWithTicket[sidx][eidx] = min(distanceWithTicket[sidx][eidx], cost/2)
			distanceWithTicket[eidx][sidx] = min(distanceWithTicket[eidx][sidx], cost/2)
		default:
			distanceWithTicket[sidx][eidx] = min(distanceWithTicket[sidx][eidx], cost)
			distanceWithTicket[eidx][sidx] = min(distanceWithTicket[eidx][sidx], cost)
		}
	}

	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if i == j {
					continue
				}
				distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
				distanceWithTicket[i][j] = min(distanceWithTicket[i][j], distanceWithTicket[i][k]+distanceWithTicket[k][j])
			}
		}
	}
	c := 0
	cWithT := 0
	for i := 0; i < M-1; i++ {
		s := cities[routes[i]]
		e := cities[routes[i+1]]
		c += distance[s][e]
		cWithT += distanceWithTicket[s][e]
	}

	if c > cWithT+R*2 {
		bw.WriteString("Yes")
	} else {
		bw.WriteString("No")
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

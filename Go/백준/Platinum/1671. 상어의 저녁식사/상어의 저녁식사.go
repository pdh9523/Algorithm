package main

import (
	"bufio"
	"os"
	"strconv"
)

type Shark struct {
	size, speed, wiz int
}

func (n Shark) unpack() (int, int, int) {
	return n.size, n.speed, n.wiz
}

func dfs(shark int, eatable [][]int, eaten []int, visit []bool) int {
	for _, other := range eatable[shark] {
		if eaten[other] == -1 {
			eaten[other] = shark
			return 1
		}
	}
	for _, other := range eatable[shark] {
		if visit[other] {
			continue
		}
		visit[other] = true
		if dfs(eaten[other], eatable, eaten, visit) == 1 {
			visit[other] = false
			eaten[other] = shark
			return 1
		}
	}
	return 0
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	arr := make([]Shark, N)
	eatable := make([][]int, N)
	eaten := make([]int, N)
	visit := make([]bool, N)
	for i := 0; i < N; i++ {
		arr[i] = Shark{input(), input(), input()}
		eatable[i] = make([]int, 0)
		eaten[i] = -1
	}

	for a := 0; a < N-1; a++ {
		aSize, aSpeed, aWiz := arr[a].unpack()
		for b := a + 1; b < N; b++ {
			bSize, bSpeed, bWiz := arr[b].unpack()
			if aSize >= bSize && aSpeed >= bSpeed && aWiz >= bWiz {
				eatable[a] = append(eatable[a], b)
			} else if aSize <= bSize && aSpeed <= bSpeed && aWiz <= bWiz {
				eatable[b] = append(eatable[b], a)
			}
		}
	}

	ans := 0
	for x := 0; x < 2; x++ {
		for i := 0; i < N; i++ {
			ans += dfs(i, eatable, eaten, visit)
		}
	}
	bw.WriteString(strconv.Itoa(N - ans))
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

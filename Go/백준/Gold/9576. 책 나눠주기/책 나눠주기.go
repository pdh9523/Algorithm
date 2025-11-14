package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type Range struct {
	start, end int
}

func (r Range) unpack() (int, int) {
	return r.start, r.end
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	tc := input()

	for t := 0; t < tc; t++ {
		N, M := input(), input()
		arr := make([]Range, M)
		for i := 0; i < M; i++ {
			arr[i] = Range{input(), input()}
		}

		sort.Slice(arr, func(i, j int) bool {
			return arr[i].end < arr[j].end
		})

		visit := make([]bool, N+1)
		ans := 0
		for i := 0; i < M; i++ {
			s, e := arr[i].unpack()
			for j := s; j <= e; j++ {
				if !visit[j] {
					visit[j] = true
					ans++
					break
				}
			}
		}

		bw.WriteString(strconv.Itoa(ans) + "\n")
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

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve() []string {
	N := intInput()
	counter := make(map[string]int)
	tree := make(map[string]string)
	for i := 0; i < N-1; i++ {
		s, e := input(), input()
		counter[s]++
		counter[e]++

		tree[s] = e
	}
	for k, v := range counter {
		if v == 1 {
			if _, exists := tree[k]; exists {
				res := make([]string, 0, N)
				now := k
				res = append(res, now)
				for {
					if _, exists := tree[now]; exists {
						now = tree[now]
						res = append(res, now)
					} else {
						break
					}
				}
				return res
			}
		}
	}
	return nil
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	for i := 1; i < N+1; i++ {
		ans := solve()
		fmt.Fprintf(bw, "Scenario #%d:\n", i)
		for _, v := range ans {
			fmt.Fprintln(bw, v)
		}
		if i != N {
			fmt.Fprintln(bw, "")
		}
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

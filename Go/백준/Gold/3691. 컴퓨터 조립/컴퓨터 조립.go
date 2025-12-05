package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt

type Value struct {
	cost, perf int
}

func min(args ...int) int {
	res := MAX_VALUE
	for _, a := range args {
		if res > a {
			res = a
		}
	}
	return res
}

func binarySearch(cost int, minPerf int, data map[string][]Value) bool {
	for _, v := range data {
		tmpCost := MAX_VALUE
		for _, x := range v {
			if x.perf >= minPerf {
				tmpCost = min(tmpCost, x.cost)
			}
		}
		if tmpCost == MAX_VALUE {
			return false
		}
		cost -= tmpCost
	}
	return cost >= 0
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	tc := intInput()
	for t := 0; t < tc; t++ {
		N, K := intInput(), intInput()
		data := make(map[string][]Value)
		for i := 0; i < N; i++ {
			t, _, c, p := input(), input(), intInput(), intInput()
			if _, exists := data[t]; !exists {
				data[t] = make([]Value, 0)
			}
			data[t] = append(data[t], Value{c, p})
		}

		left, right := 0, 1_000_000_000
		for left < right {
			mid := (left + right + 1) / 2
			if binarySearch(K, mid, data) {
				left = mid
			} else {
				right = mid - 1
			}
		}
		bw.WriteString(strconv.Itoa(left) + "\n")
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

package main

import (
	"bufio"
	"os"
	"strconv"
)

func max(args ...int) int {
	res := 0
	for _, arg := range args {
		if res < arg {
			res = arg
		}
	}
	return res
}

func getSet(args ...int) map[int]bool {
	res := make(map[int]bool)
	for _, arg := range args {
		res[arg] = true
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = intInput()
	}
	s := getSet(arr...)
	maxValue := max(arr...)

	ans := make([]int, maxValue+1)

	for _, a := range arr {
		for x := 2 * a; x < maxValue+1; x += a {
			if _, exists := s[x]; exists {
				ans[a]++
				ans[x]--
			}
		}
	}

	for _, a := range arr {
		bw.WriteString(strconv.Itoa(ans[a]) + " ")
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

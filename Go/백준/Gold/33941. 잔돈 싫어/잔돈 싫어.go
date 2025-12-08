package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	const mod = 500

	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()

	DP := make([]int, mod)
	for i := 1; i < mod; i++ {
		DP[i] = -1
	}
	tmp := make([]int, mod)

	ans := 0

	for i := 0; i < N; i++ {
		card := intInput()
		if card >= 20000 || card <= 500 {
			continue
		}

		val := card - 500

		if val%mod == 0 {
			ans += val
			continue
		}

		copy(tmp, DP)

		for r := 0; r < mod; r++ {
			if DP[r] < 0 {
				continue
			}
			nr := (r + val) % mod
			nv := DP[r] + val
			if nv > tmp[nr] {
				tmp[nr] = nv
			}
		}

		DP, tmp = tmp, DP
	}

	if DP[0] < 0 {
		DP[0] = 0
	}

	fmt.Fprintln(bw, ans+DP[0])
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

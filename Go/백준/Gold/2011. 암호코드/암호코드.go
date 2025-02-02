package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func main() {
	defer bw.Flush()

	N := input()

	if int(N[0]-'0') == 0 {
		bw.WriteString("0")
		return
	}

	arr := make([]int, len(N)+1)
	for i := 1; i <= len(N); i++ {
		arr[i] = int(N[i-1] - '0')
	}

	DP := make([]int, len(arr))
	DP[0] = 1
	DP[1] = 1
	for i := 2; i < len(arr); i++ {
		if arr[i] != 0 {
			DP[i] += DP[i-1]
		}
		tmp := arr[i] + arr[i-1]*10
		if 10 <= tmp && tmp <= 26 {
			DP[i] += DP[i-2]
		}
		if DP[i] == 0 {
			break
		}
		DP[i] %= 1000000
	}
	bw.WriteString(fmt.Sprintln(DP[len(DP)-1]))
}

// fastIO
func input() string {
	bs.Scan()
	return bs.Text()
}

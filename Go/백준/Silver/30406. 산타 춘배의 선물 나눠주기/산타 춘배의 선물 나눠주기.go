package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
	dx = []int{0, 1, 0, 1, 0, 2}
	dy = []int{3, 2, 2, 3, 1, 3}
)

func inputInt() int {
	bs.Scan()
	n, _ := strconv.Atoi(bs.Text())
	return n
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := inputInt()
	data := make([]int, 4)

	for i := 0; i < N; i++ {
		data[inputInt()]++
	}
	ans := 0
	for i := 0; i < 6; i++ {
		tmp := min(data[dx[i]], data[dy[i]])
		ans += tmp * (dx[i] ^ dy[i])
		data[dx[i]] -= tmp
		data[dy[i]] -= tmp
	}
	bw.WriteString(strconv.Itoa(ans))
}

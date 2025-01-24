package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func main() {
	line, _, _ := br.ReadLine()
	N, _ := strconv.Atoi(string(line))

	arr := make([]int, N)
	for i := 0; i < N; i++ {
		line, _, _ := br.ReadLine()
		arr[i], _ = strconv.Atoi(string(line))
	}

	sort.Ints(arr)

	for i := range arr {
		bw.WriteString(strconv.Itoa(arr[i]))
		bw.WriteString("\n")
	}

	bw.Flush()
}

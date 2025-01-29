package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, _ := strconv.Atoi(input())

	data := make(map[string]int)
	for i := 0; i < N; i++ {
		ingredient := input()
		gram, _ := strconv.Atoi(input())
		data[ingredient] += gram
	}

	for aK, aV := range data {
		for bK, bV := range data {
			if aK == bK {
				continue
			}
			if int(float32(aV)*1.618) == bV {
				bw.WriteString("Delicious!")
				return
			}
		}
	}
	bw.WriteString("Not Delicious...")
}

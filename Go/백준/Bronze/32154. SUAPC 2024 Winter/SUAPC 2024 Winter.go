package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	data := make([][]string, 11)
	data[1] = []string{"A", "B", "C", "D", "E", "F", "G", "H", "J", "L", "M"}
	data[2] = []string{"A", "C", "E", "F", "G", "H", "I", "L", "M"}
	data[3] = []string{"A", "C", "E", "F", "G", "H", "I", "L", "M"}
	data[4] = []string{"A", "B", "C", "E", "F", "G", "H", "L", "M"}
	data[5] = []string{"A", "C", "E", "F", "G", "H", "L", "M"}
	data[6] = []string{"A", "C", "E", "F", "G", "H", "L", "M"}
	data[7] = []string{"A", "C", "E", "F", "G", "H", "L", "M"}
	data[8] = []string{"A", "C", "E", "F", "G", "H", "L", "M"}
	data[9] = []string{"A", "C", "E", "F", "G", "H", "L", "M"}
	data[10] = []string{"A", "B", "C", "F", "G", "H", "L", "M"}

	N := intInput()
	bw.WriteString(strconv.Itoa(len(data[N])) + "\n")
	for _, x := range data[N] {
		bw.WriteString(x + " ")
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

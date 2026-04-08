package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt

func max(args ...int) int {
	res := 0
	for _, arg := range args {
		if res < arg {
			res = arg
		}
	}
	return res
}

func min(args ...int) int {
	res := MAX_VALUE
	for _, arg := range args {
		if res > arg {
			res = arg
		}
	}
	return res
}

func inRange(start, end int, target float64) bool {
	if float64(start) <= target && target <= float64(end) {
		return true
	}
	return false
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	hLo, hHi := intInput(), intInput()
	sLo, sHi := intInput(), intInput()
	vLo, vHi := intInput(), intInput()

	R, G, B := intInput(), intInput(), intInput()
	M := max(R, G, B)
	var m float64 = float64(min(R, G, B))

	var V float64 = float64(M)
	var S float64 = 255 * (V - m) / V

	var H float64
	switch V {
	case float64(R):
		H = 60 * float64(G-B) / (V - m)
	case float64(G):
		H = 120 + (60 * float64(B-R) / (V - m))
	default:
		H = 240 + (60 * float64(R-G) / (V - m))
	}

	if H < 0 {
		H += 360
	}

	if inRange(hLo, hHi, H) && inRange(sLo, sHi, S) && inRange(vLo, vHi, V) {
		bw.WriteString("Lumi will like it.")
	} else {
		bw.WriteString("Lumi will not like it.")
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

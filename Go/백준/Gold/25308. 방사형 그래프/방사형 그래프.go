package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const size = 8

var ans = 0

func isRound(res []int) bool {
	var firstSign int

	for i := 0; i < size; i++ {
		prev := (i + size - 1) % size
		next := (i + 1) % size

		angle_prev := 2.0 * math.Pi * float64(prev) / float64(size)
		angle_i := 2.0 * math.Pi * float64(i) / float64(size)
		angle_next := 2.0 * math.Pi * float64(next) / float64(size)

		x_prev := float64(res[prev]) * math.Cos(angle_prev)
		y_prev := float64(res[prev]) * math.Sin(angle_prev)
		x_i := float64(res[i]) * math.Cos(angle_i)
		y_i := float64(res[i]) * math.Sin(angle_i)
		x_next := float64(res[next]) * math.Cos(angle_next)
		y_next := float64(res[next]) * math.Sin(angle_next)

		v1_x := x_i - x_prev
		v1_y := y_i - y_prev
		v2_x := x_next - x_i
		v2_y := y_next - y_i

		cross := v1_x*v2_y - v1_y*v2_x

		var sign int
		if cross > 1e-9 {
			sign = 1
		} else if cross < -1e-9 {
			sign = -1
		} else {
			sign = 0
		}

		if i == 0 {
			firstSign = sign
		} else if sign != 0 && firstSign != 0 && sign != firstSign {
			return false
		}
	}
	return true
}

func backtrack(idx int, visit int, res, arr []int) {
	if idx == size {
		if isRound(res) {
			ans++
			return
		}
	}
	for i := 0; i < size; i++ {
		if (1<<i)&visit == 0 {
			res[idx] = arr[i]
			backtrack(idx+1, visit|(1<<i), res, arr)
			res[idx] = 0
		}
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = input()
	}
	backtrack(0, 0, make([]int, size), arr)
	bw.WriteString(strconv.Itoa(ans))
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}

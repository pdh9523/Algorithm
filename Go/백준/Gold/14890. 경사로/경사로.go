package main

import (
	"bufio"
	"os"
	"strconv"
)

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func check(line []int, size int) bool {
	for i := 0; i < len(line)-1; i++ {
		if abs(line[i]-line[i+1]) > 1 {
			return false
		}
	}
	prev := line[0]
	cnt := 1
	idx := 1
	for idx < len(line) {
		now := line[idx]
		if prev == now {
			cnt++
			idx++
		} else if prev > now {
			cnt = 0
			for idx < len(line) && now == line[idx] && cnt < size {
				cnt++
				prev = line[idx]
				idx++
			}
			if cnt < size {
				return false
			}
			cnt = 0
		} else if prev < now {
			if cnt < size {
				return false
			}
			cnt = 1
			prev = line[idx]
			idx++
		}
	}
	return true
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, L := input(), input()

	arr := make([][]int, N)
	for i := 0; i < N; i++ {
		arr[i] = make([]int, N)
		for j := 0; j < N; j++ {
			arr[i][j] = input()
		}
	}
	ans := 0
	vertical := make([]int, N)
	for i := 0; i < N; i++ {
		if check(arr[i], L) {
			ans++
		}
		for j := 0; j < N; j++ {
			vertical[j] = arr[j][i]
		}
		if check(vertical, L) {
			ans++
		}
	}
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

package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const SIZE = 2000001

func getPrime() []bool {
	isPrime := make([]bool, SIZE)
	for i := 2; i < int(math.Sqrt(SIZE))+1; i++ {
		if isPrime[i] {
			continue
		}
		for j := i * i; j < SIZE; j += i {
			isPrime[j] = true
		}
	}
	return isPrime
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	isPrime := getPrime()

	N := input()
	arr := make([]int, N)

	for i := 0; i < N; i++ {
		arr[i] = input()
	}
	ans := 0
	for i := 2; i < SIZE; i++ {
		if isPrime[i] {
			continue
		}
		if ans*i > arr[N-1] {
			break
		}
		data := make(map[int]int)
		for j := 0; j < N; j++ {
			tmp := arr[j] % i
			data[tmp]++
		}
		for _, v := range data {
			ans = max(ans, v)
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

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const SIZE = 1_000_001

func getPrimes() []int {
	isPrime := make([]bool, SIZE)
	for i := 0; i < SIZE; i++ {
		isPrime[i] = true
	}
	for i := 2; i < int(math.Sqrt(SIZE))+1; i++ {
		if isPrime[i] {
			for j := i * 2; j < SIZE; j += i {
				isPrime[j] = false
			}
		}
	}
	res := make([]int, 0)
	for i := 2; i < SIZE; i++ {
		if isPrime[i] {
			res = append(res, i)
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	primes := getPrimes()
	N := intInput()
	cnt := 0

	for _, p := range primes {
		for N%p == 0 {
			N /= p
			cnt++
		}
		if N == 1 {
			break
		}
	}
	fmt.Println(math.Ceil((math.Log2(float64(cnt)))))
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

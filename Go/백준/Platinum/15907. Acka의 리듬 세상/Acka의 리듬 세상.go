package main

import (
	"bufio"
	"os"
	"strconv"
)

const SIZE = 2000001

func getPrime() []bool {
	isPrime := make([]bool, SIZE)
	for i := 2; i < 1415; i++ {
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
	ans := 0
	for i := 0; i < N; i++ {
		arr[i] = input()
		if arr[i]%2 == 0 {
			ans++
		}
	}
	ans = max(ans, N-ans)
	check := make([]int, SIZE)
	cnt := make([]int, SIZE)
	for i := 3; i < SIZE; i++ {
		if isPrime[i] {
			continue
		}
		for j := 0; j < N; j++ {
			tmp := arr[j] % i
			if check[tmp] != i {
				check[tmp] = i
				cnt[tmp] = 1
			} else {
				cnt[tmp]++
				ans = max(ans, cnt[tmp])
			}
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

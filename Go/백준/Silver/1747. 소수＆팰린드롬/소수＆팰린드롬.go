package main

import (
	"bufio"
	"os"
	"strconv"
)

const maxValue = 2000000

func getPrime() map[int]bool {
	primes := make(map[int]bool)
	for i := 2; i <= maxValue; i++ {
		primes[i] = true
	}

	for i := 2; i <= maxValue; i++ {
		if primes[i] {
			nxt := i * i
			for nxt <= maxValue {
				delete(primes, nxt)
				nxt += i
			}
		}
	}
	return primes
}

func isPalin(num int) bool {
	str := strconv.Itoa(num)

	for i := 0; i < len(str); i++ {
		if str[i] != str[len(str)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	primes := getPrime()
	for i := N; i < maxValue; i++ {
		if _, exists := primes[i]; exists {
			if isPalin(i) {
				bw.WriteString(strconv.Itoa(i))
				return
			}
		}
	}
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

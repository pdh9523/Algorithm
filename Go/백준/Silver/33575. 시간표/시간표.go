package main

import (
	"bufio"
	"os"
	"strconv"
)

type Set map[int]bool

func (s Set) Add(key int) {
	s[key] = true
}

func (s Set) Remove(key int) {
	delete(s, key)
}

func (s Set) Has(key int) bool {
	return s[key]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, _, A, B := input(), input(), input(), input()

	table := make([]int, N+1)
	for i := 0; i < N; i++ {
		table[i] = input()
	}
	table[N] = -1
	like := make(Set)
	for i := 0; i < A; i++ {
		like.Add(input())
	}
	dislike := make(Set)
	for i := 0; i < B; i++ {
		dislike.Add(input())
	}

	isLike := true
	cnt := 0
	ans := 0
	for _, v := range table {
		if like.Has(v) {
			if isLike {
				cnt++
			} else {
				if cnt >= 3 {
					ans -= cnt
				}
				isLike = true
				cnt = 1
			}
		} else if dislike.Has(v) {
			if !isLike {
				cnt++
			} else {
				if cnt >= 3 {
					ans += cnt
				}
				isLike = false
				cnt = 1
			}
		} else {
			if cnt >= 3 {
				if isLike {
					ans += cnt
				} else {
					ans -= cnt
				}
			}
			cnt = 0
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

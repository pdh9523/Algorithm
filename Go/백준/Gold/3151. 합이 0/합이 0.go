package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func getComb(a int64, b int64) int64 {
	var div, mod int64
	div, mod = 1, 1
	for i := a; i > a-b; i-- {
		div *= int64(i)
	}

	for i := 1; i <= int(b); i++ {
		mod *= int64(i)
	}

	return div / mod
}

func main() {
	bs.Split(bufio.ScanWords)

	N := input()
	arr := make([]int, 0)
	counter := make(map[int]int64)
	for i := 0; i < N; i++ {

		num := input()
		if _, exists := counter[num]; !exists {
			arr = append(arr, num)
		}
		counter[num]++
	}
	N = len(arr)
	sort.Ints(arr)
	var ans int64
	ans = 0
	for i := 0; i < N; i++ {
		left := i
		right := N - 1
		for left <= right {
			now := arr[i] + arr[left] + arr[right]
			if now > 0 {
				right--
			} else if now < 0 {
				left++
			} else {
				if i == left {
					if i == right {
						ans += getComb(counter[arr[i]], 3)
					} else {
						ans += getComb(counter[arr[i]], 2) * counter[arr[right]]
					}
				} else if i == right {
					ans += getComb(counter[arr[i]], 2) * counter[arr[left]]
				} else if left == right {
					ans += getComb(counter[arr[left]], 2) * counter[arr[i]]
				} else {
					ans += counter[arr[i]] * counter[arr[left]] * counter[arr[right]]
				}

				left++
				right--
			}
		}
	}
	fmt.Println(ans)
}

var bs = bufio.NewScanner(os.Stdin)

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}

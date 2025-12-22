package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func getCountWithKeys(arr []int) (map[int]int64, []int) {
	size := len(arr)
	counter := make(map[int]int64)
	prefixSum := make([]int, size+1)
	for i := 1; i < size+1; i++ {
		prefixSum[i] = prefixSum[i-1] + arr[i-1]
		for j := 0; j < i; j++ {
			x := prefixSum[i] - prefixSum[j]
			counter[x]++
		}
	}

	keys := make([]int, 0, len(counter))
	for k := range counter {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	return counter, keys
}

func binarySearch(arr []int, target int) bool {
	left, right := 0, len(arr)
	for left < right {
		mid := (left + right) / 2
		if arr[mid] > target {
			right = mid
		} else if arr[mid] < target {
			left = mid + 1
		} else {
			return true
		}
	}
	return false
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	T := intInput()

	arr := getArray(intInput())
	brr := getArray(intInput())

	aCounter, aKeys := getCountWithKeys(arr)
	bCounter, bKeys := getCountWithKeys(brr)

	var ans int64 = 0
	for _, a := range aKeys {
		b := T - a
		if binarySearch(bKeys, b) {
			ans += aCounter[a] * bCounter[b]
		}
	}
	fmt.Fprintln(bw, ans)
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func getArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = intInput()
	}
	return arr
}

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

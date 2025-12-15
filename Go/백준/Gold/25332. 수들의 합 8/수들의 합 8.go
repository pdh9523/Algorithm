package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func getPrefixSum(arr []int) []int64 {
	res := make([]int64, len(arr))
	res[0] = int64(arr[0])
	for i := 1; i < len(arr); i++ {
		res[i] = res[i-1] + int64(arr[i])
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	arr := getArray(N)
	brr := getArray(N)
	psArr := make([]int64, N+1)
	psBrr := make([]int64, N+1)

	data := make(map[int64]int64)
	var ans int64
	ans = 0
	for i := 1; i < N+1; i++ {
		psArr[i] = psArr[i-1] + int64(arr[i-1])
		psBrr[i] = psBrr[i-1] + int64(brr[i-1])

		if psArr[i] == psBrr[i] {
			ans++
		}
		if _, exists := data[psArr[i]-psBrr[i]]; !exists {
			data[psArr[i]-psBrr[i]] = 0
		}
		ans += data[psArr[i]-psBrr[i]]
		data[psArr[i]-psBrr[i]]++
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

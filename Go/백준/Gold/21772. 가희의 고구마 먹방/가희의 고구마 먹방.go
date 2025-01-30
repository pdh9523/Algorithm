package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)

	dx = [4]int{0, 1, 0, -1}
	dy = [4]int{1, 0, -1, 0}

	ans = 0
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func inputInt() int {
	res, _ := strconv.Atoi(input())
	return res
}

func find(char uint8, N, M int, arr []string) (int, int) {
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if arr[i][j] == char {
				return i, j
			}
		}
	}
	return -1, -1
}

func hashing(x, y int) string {
	return strconv.Itoa(x) + "," + strconv.Itoa(y)
}

func backtrack(idx, x, y, N, M, K int, arr []string, result map[string]bool) {
	if idx == K {
		ans = max(ans, len(result))
		return
	}

	if len(result)+(K-idx) <= ans {
		return
	}

	for i := 0; i < 4; i++ {
		nx, ny := x+dx[i], y+dy[i]
		if 0 <= nx && nx < N && 0 <= ny && ny < M {
			if arr[nx][ny] == '#' {
				continue
			}
			key := hashing(nx, ny)

			if _, exists := result[key]; !exists && arr[nx][ny] == 'S' {
				result[key] = true
				backtrack(idx+1, nx, ny, N, M, K, arr, result)
				delete(result, key)
			} else {
				backtrack(idx+1, nx, ny, N, M, K, arr, result)
			}
		}
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M, K := inputInt(), inputInt(), inputInt()
	arr := make([]string, N)
	for i := 0; i < N; i++ {
		arr[i] = input()
	}
	si, sj := find('G', N, M, arr)
	backtrack(0, si, sj, N, M, K, arr, make(map[string]bool))

	bw.WriteString(strconv.Itoa(ans))
}

package main

import (
	"bufio"
	"container/list"
	"os"
	"strconv"
)

const size = 3

type Node struct {
	x, y int
	code string
}

func (n Node) unpack() (int, int, string) {
	return n.x, n.y, n.code
}

var (
	dx = [4]int{0, 1, 0, -1}
	dy = [4]int{1, 0, -1, 0}
)

func hash(arr [][]int) string {
	res := ""
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr); j++ {
			res += strconv.Itoa(arr[i][j])
		}
	}
	return res
}

func decode(x string) [][]int {
	res := make([][]int, size)
	for i := 0; i < size; i++ {
		res[i] = make([]int, size)
		for j := 0; j < size; j++ {
			res[i][j], _ = strconv.Atoi(string(x[(i*3)+j]))
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	sx, sy, arr := getArray()
	visit := make(map[string]int)

	visit[hash(arr)] = 0
	q := list.New()
	q.PushBack(Node{sx, sy, hash(arr)})
	for q.Len() > 0 {
		x, y, h := q.Remove(q.Front()).(Node).unpack()
		if h == "123456780" {
			bw.WriteString(strconv.Itoa(visit[h]))
			return
		}
		a := decode(h)
		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if 0 <= nx && nx < size && 0 <= ny && ny < size {
				a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
				key := hash(a)
				if _, exists := visit[key]; !exists {
					visit[key] = visit[h] + 1
					q.PushBack(Node{nx, ny, key})
				}
				a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
			}
		}
	}
	bw.WriteString("-1")
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func getArray() (int, int, [][]int) {
	var sx, sy int
	arr := make([][]int, size)
	for i := 0; i < size; i++ {
		arr[i] = make([]int, size)
		for j := 0; j < size; j++ {
			arr[i][j] = intInput()
			if arr[i][j] == 0 {
				sx, sy = i, j
			}
		}
	}
	return sx, sy, arr
}

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

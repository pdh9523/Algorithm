package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type Lecture struct {
	value, idx int
}

func (l Lecture) unpack() (int, int) {
	return l.value, l.idx
}

type Lectures []Lecture

func (l Lectures) Len() int { return len(l) }
func (l Lectures) Less(i, j int) bool {
	return l[i].value < l[j].value
}
func (l Lectures) Swap(i, j int) { l[i], l[j] = l[j], l[i] }

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	arr := make([]Lecture, 0)
	for i := 0; i < M; i++ {
		tmp := input()
		if tmp <= 2*N {
			arr = append(arr, Lecture{tmp, i + 1})
			if N <= tmp {
				bw.WriteString("1\n" + strconv.Itoa(i+1))
				return
			}
		}
	}
	sort.Sort(sort.Reverse(Lectures(arr)))
	ans := make([]int, 0)
	now := 0
	for i := 0; i < len(arr); i++ {
		value, idx := arr[i].unpack()
		if now+value <= N*2 {
			ans = append(ans, idx)
			now += value
		}
		if now >= N {
			break
		}
	}
	bw.WriteString(strconv.Itoa(len(ans)) + "\n")
	for i := 0; i < len(ans); i++ {
		bw.WriteString(strconv.Itoa(ans[i]) + "\n")
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

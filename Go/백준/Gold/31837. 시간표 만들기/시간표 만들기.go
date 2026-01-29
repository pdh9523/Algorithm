package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Lecture struct {
	score     int
	startTime int
	endTime   int
}

type Part struct {
	time    int
	checker int
}

func parseTime(day int, timeStr string) int {
	t := strings.Split(timeStr, ":")
	return day*100000 + toInt(t[0])*60 + toInt(t[1])
}

func hasOverlap(selected []Lecture) bool {
	if len(selected) == 0 {
		return false
	}

	var events []Part
	for _, lec := range selected {
		events = append(events, Part{lec.startTime, 1})
		events = append(events, Part{lec.endTime, -1})
	}

	sort.Slice(events, func(i, j int) bool {
		if events[i].time == events[j].time {
			return events[i].checker < events[j].checker
		}
		return events[i].time < events[j].time
	})

	count := 0
	for _, e := range events {
		count += e.checker
		if count > 1 {
			return true
		}
	}
	return false
}

func backtrack(idx int, arr [][]Lecture, selected []Lecture, score int) {
	if score > 22 {
		return
	}

	if idx == len(arr) {
		if score == 22 && !hasOverlap(selected) {
			ans++
		}
		return
	}

	backtrack(idx+1, arr, selected, score)
	for _, lecture := range arr[idx] {
		backtrack(idx+1, arr, append(selected, lecture), score+lecture.score)
	}
}

var ans = 0

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := intInput()
	arr := make([][]Lecture, N)
	for i := 0; i < N; i++ {
		size := intInput()
		arr[i] = make([]Lecture, size)
		for j := 0; j < size; j++ {
			c, d, s, e := intInput(), intInput(), input(), input()
			startTime, endTime := parseTime(d, s), parseTime(d, e)
			arr[i][j] = Lecture{c, startTime, endTime}
		}
	}

	backtrack(0, arr, nil, 0)
	fmt.Fprintln(bw, ans)
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
	return toInt(input())
}

func toInt(str string) int {
	num, _ := strconv.Atoi(str)
	return num
}

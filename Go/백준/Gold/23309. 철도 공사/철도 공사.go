package main

import (
	"bufio"
	"os"
	"strconv"
)

type Node struct {
	value int
	prev  *Node
	next  *Node
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := intInput(), intInput()

	stations := make([]int, N)
	for i := 0; i < N; i++ {
		stations[i] = intInput()
	}

	cursor := make(map[int]*Node)
	nodes := make([]*Node, N)
	for i := 0; i < N; i++ {
		nodes[i] = &Node{value: stations[i]}
		cursor[stations[i]] = nodes[i]
	}
	for i := 0; i < N; i++ {
		nodes[i].prev = nodes[(i-1+N)%N]
		nodes[i].next = nodes[(i+1)%N]
	}

	for i := 0; i < M; i++ {
		op := input()

		if op == "BN" {
			stationI, stationJ := intInput(), intInput()
			now := cursor[stationI]
			nxt := now.next

			newNode := &Node{value: stationJ}
			cursor[stationJ] = newNode

			newNode.prev = now
			newNode.next = nxt
			now.next = newNode
			nxt.prev = newNode

			bw.WriteString(strconv.Itoa(nxt.value) + "\n")

		} else if op == "BP" {
			stationI, stationJ := intInput(), intInput()
			now := cursor[stationI]
			prev := now.prev

			newNode := &Node{value: stationJ}
			cursor[stationJ] = newNode

			newNode.prev = prev
			newNode.next = now
			now.prev = newNode
			prev.next = newNode

			bw.WriteString(strconv.Itoa(prev.value) + "\n")

		} else if op == "CN" {
			stationI := intInput()
			now := cursor[stationI]
			target := now.next

			now.next = target.next
			target.next.prev = now

			delete(cursor, target.value)
			bw.WriteString(strconv.Itoa(target.value) + "\n")

		} else {
			stationI := intInput()
			now := cursor[stationI]
			target := now.prev

			now.prev = target.prev
			target.prev.next = now

			delete(cursor, target.value)
			bw.WriteString(strconv.Itoa(target.value) + "\n")
		}
	}
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
	num, _ := strconv.Atoi(input())
	return num
}

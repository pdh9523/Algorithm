package main

import (
	"bufio"
	"os"
	"strconv"
)

type Node struct {
	children []*Node
	cnt      int64
}

func Ctoi(c rune) int {
	return int(c - 'a')
}

type Trie struct {
	root *Node
}

func (t *Trie) Insert(s string) {
	runes := []rune(s)

	now := t.root
	for _, char := range runes {
		idx := Ctoi(char)
		if now.children[idx] == nil {
			now.children[idx] = newNode()
		}
		now = now.children[idx]
		now.cnt++
	}
}

func newTrie() *Trie {
	return &Trie{newNode()}
}

func newNode() *Node {
	return &Node{make([]*Node, 26), 0}
}

const (
	MOD  = 1000000007
	size = 26
)

func main() {
	bs.Buffer(buf, 250000)
	bs.Split(bufio.ScanWords)

	defer bw.Flush()

	trie := newTrie()
	N := intInput()
	for i := 0; i < N; i++ {
		trie.Insert(input())
	}

	word := input()
	length := len(word)

	DP := make([]int64, length+1)
	DP[0] = 1
	for i := 0; i < length; i++ {
		now := trie.root
		for j := i; j < length; j++ {
			idx := Ctoi(rune(word[j]))
			if now.children[idx] == nil {
				break
			}
			now = now.children[idx]
			DP[j+1] = (DP[i]*now.cnt + DP[j+1]) % MOD
		}
	}
	bw.WriteString(strconv.Itoa(int(DP[length])))
}

var (
	bs  = bufio.NewScanner(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	buf = make([]byte, 250000)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

package main

import (
	"bufio"
	"os"
	"strconv"
)

type Pair struct {
	val, idx int
}

func (p Pair) unpack() (int, int) {
	return p.val, p.idx
}

type SegTree[T any] struct {
	size  int
	tree  []T
	merge func(T, T) T
}

func NewSegTree[T any](arr []T, merge func(T, T) T) *SegTree[T] {
	size := len(arr)
	tree := make([]T, size*2)
	copy(tree[size:], arr)

	s := &SegTree[T]{size: size, tree: tree, merge: merge}
	s.init()
	return s
}

func (s *SegTree[T]) init() {
	for i := s.size - 1; i >= 1; i-- {
		s.tree[i] = s.merge(s.tree[i*2], s.tree[i*2+1])
	}
}

func (s *SegTree[T]) Query(l, r int) T {
	l += s.size
	r += s.size

	var resL, resR T
	hasL, hasR := false, false

	for l < r {
		if l&1 == 1 {
			if hasL {
				resL = s.merge(resL, s.tree[l])
			} else {
				resL = s.tree[l]
				hasL = true
			}
			l++
		}
		if r&1 == 1 {
			r--
			if hasR {
				resR = s.merge(s.tree[r], resR)
			} else {
				resR = s.tree[r]
				hasR = true
			}
		}
		l >>= 1
		r >>= 1
	}

	if !hasL {
		return resR
	}
	if !hasR {
		return resL
	}
	return s.merge(resL, resR)
}

func find(tree *SegTree[Pair], left int, right int) {
	if left > right {
		return
	}

	height, idx := tree.Query(left, right+1).unpack()

	ans = max(ans, height*(right-left+1))
	find(tree, left, idx-1)
	find(tree, idx+1, right)
}

var ans = 0

func main() {
	bs.Buffer(buf, 1_000_000)
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	N := intInput()

	arr := make([]Pair, N)
	for i := 0; i < N; i++ {
		arr[i] = Pair{intInput(), i}
	}

	tree := NewSegTree(arr, func(a, b Pair) Pair {
		if a.val <= b.val {
			return a
		}
		return b
	})
	find(tree, 0, N-1)

	bw.WriteString(strconv.Itoa(ans))
}

var (
	bs  = bufio.NewScanner(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	buf = make([]byte, 1_000_000)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func intInput() int {
	num, _ := strconv.Atoi(input())
	return num
}

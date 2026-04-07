package main

import (
    "fmt"
    "strconv"
    "os"
    "bufio"
    "math"
)

func abs(num int) int {
    if num < 0 {
        num *= -1
    }
    return num
}

func calc(p, m, c int) int {
    return (p+m)*(m+c)
}

func main() {
    defer bw.Flush()
    bs.Split(bufio.ScanWords)
    
    P, M, C := input(), input(), input()
    X := input()
    
    ans := math.MaxInt
    for p:=1; p<=P; p++ {
         for m:=1; m<=M; m++ {
             for c:=1; c<=C; c++ {
                 ans = min(ans, abs(calc(p,m,c)-X))
             }
         }
    }
    
    fmt.Fprintln(bw, ans)
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
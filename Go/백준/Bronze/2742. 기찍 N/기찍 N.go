package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	br := bufio.NewReader(os.Stdin)
	line, _, _ := br.ReadLine()
	a, _ := strconv.Atoi(string(line))
	
	bw := bufio.NewWriterSize(os.Stdout, a)
	defer bw.Flush()

	for i := a; i > 0; i-- {
		bw.WriteString(strconv.Itoa(i))
		bw.WriteString("\n")
	}
}

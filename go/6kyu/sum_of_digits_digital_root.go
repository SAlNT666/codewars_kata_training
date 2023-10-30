// https://www.codewars.com/kata/541c8630095125aba6000c00

package main

import "fmt"

func DigitalRoot(n int) int {
	return (n-1)%9 + 1
}

func main() {
	fmt.Println(DigitalRoot(195), 6)
}

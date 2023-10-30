// https://www.codewars.com/kata/50654ddff44f800200000004

package main

import "fmt"

func Multiply(a, b int) int {
	return a * b
}

func main() {
	fmt.Println(Multiply(1, 0), 0)
	fmt.Println(Multiply(5, 8), 40)
}

// https://www.codewars.com/kata/52503c77e5b972f21600000e

package main

import "fmt"

func main() {
	fmt.Println(LargestDifference([]int{9, -4, 1, 10, 3, 4, 1, -6, -2}))
}

func LargestDifference(a []int) int {
	for n := len(a) - 1; n > 0; n-- {
		for i := 0; i < len(a)-n; i++ {
			if a[i] <= a[i+n] {
				return n
			}
		}
	}

	return 0
}

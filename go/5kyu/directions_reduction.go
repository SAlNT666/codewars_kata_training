// https://www.codewars.com/kata/550f22f4d758534c1100025a

package main

import (
	"fmt"
)

func DirReduc(arr []string) []string {
	opposites := map[string]string{
		"NORTH": "SOUTH",
		"SOUTH": "NORTH",
		"EAST":  "WEST",
		"WEST":  "EAST",
	}

	var reduced []string
	for _, dir := range arr {
		if len(reduced) > 0 && reduced[len(reduced)-1] == opposites[dir] {
			reduced = reduced[:len(reduced)-1]
		} else {
			reduced = append(reduced, dir)
		}
	}

	return reduced
}

func main() {
	fmt.Println(DirReduc([]string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}), []string{"WEST"})
}

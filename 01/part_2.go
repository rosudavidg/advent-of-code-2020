package main

import (
	"fmt"
	"strconv"

	"../utils/reader"
)

func main() {
	var numbers []int
	target := 2020

	for _, line := range reader.ReadInput() {
		if line != "" {

			number, _ := strconv.Atoi(line)
			numbers = append(numbers, number)
		}
	}

	var usedNumbers []int

	for _, number := range numbers {
		for i := 0; i < len(usedNumbers)-1; i++ {
			for j := i + 1; j < len(usedNumbers); j++ {
				if number+usedNumbers[i]+usedNumbers[j] == target {
					fmt.Printf("%d\n", number*usedNumbers[i]*usedNumbers[j])
					return
				}
			}
		}

		usedNumbers = append(usedNumbers, number)
	}
}

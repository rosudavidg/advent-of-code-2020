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
		for _, usedNumber := range usedNumbers {
			if number+usedNumber == target {
				fmt.Printf("%d\n", number*usedNumber)
				return
			}
		}

		usedNumbers = append(usedNumbers, number)
	}
}

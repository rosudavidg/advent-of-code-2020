package main

import (
	"fmt"
	"strconv"
	"strings"

	"../utils/reader"
)

func is_valid(text string, character byte, start, stop int) bool {
	counter := 0

	for i := range text {
		if text[i] == character {
			counter++
		}
	}

	return start <= counter && counter <= stop
}

func main() {
	validCount := 0
	input := reader.ReadInput()

	for _, line := range input {
		if line != "" {

			splitted := strings.Split(line, ":")
			text := strings.TrimSpace(splitted[1])

			splitted = strings.Split(splitted[0], " ")
			character := splitted[1][0]

			splitted = strings.Split(splitted[0], "-")
			start, _ := strconv.Atoi(splitted[0])
			stop, _ := strconv.Atoi(splitted[1])

			if is_valid(text, character, start, stop) {
				validCount++
			}
		}
	}

	fmt.Println(validCount)
}

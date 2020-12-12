package reader

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func ReadInput() []string {
	fileBytes, err := ioutil.ReadFile("file.in")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	sliceData := strings.Split(string(fileBytes), "\n")

	return sliceData
}

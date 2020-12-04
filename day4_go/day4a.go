package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
)

func parsePassportsLines(dat string) []string {
	lines := regexp.MustCompile("\r?\n ?\r?\n").Split(dat, -1)

	return lines
}

func checkPassportIsValid(passport string) bool {
	rgByr := regexp.MustCompile("(?i)byr:([^ ]+)")
	rgIyr := regexp.MustCompile("(?i)iyr:([^ ]+)")
	rgEyr := regexp.MustCompile("(?i)eyr:([^ ]+)")
	rgHgt := regexp.MustCompile("(?i)hgt:([^ ]+)")
	rgHcl := regexp.MustCompile("(?i)hcl:([^ ]+)")
	rgEcl := regexp.MustCompile("(?i)ecl:([^ ]+)")
	rgPid := regexp.MustCompile("(?i)pid:([^ ]+)")
	//rgCid := regexp.MustCompile("(?im)cid:([0-9]+)")

	numberOfByr := len(rgByr.FindAllString(passport, -1))
	numberOfIyr := len(rgIyr.FindAllString(passport, -1))
	numberOfEyr := len(rgEyr.FindAllString(passport, -1))
	numberOfHgt := len(rgHgt.FindAllString(passport, -1))
	numberOfHcl := len(rgHcl.FindAllString(passport, -1))
	numberOfEcl := len(rgEcl.FindAllString(passport, -1))
	numberOfPid := len(rgPid.FindAllString(passport, -1))
	//numberOfCid := len(rgCid.FindAllString(passport, -1))

	if numberOfByr >= 1 && numberOfIyr >= 1 && numberOfEyr >= 1 && numberOfHgt >= 1 && numberOfHcl >= 1 && numberOfEcl >= 1 && numberOfPid >= 1 {
		return true
	}

	return false
}

func main() {
	dat, _ := ioutil.ReadFile("input4.txt")

	passportsAsString := parsePassportsLines(string(dat))

	totalCount := 0
	validCount := 0
	for _, passport := range passportsAsString {
		isValid := checkPassportIsValid(passport)
		if isValid {
			validCount++
		}
		totalCount++
	}

	fmt.Printf("total passports: %d\nvalid passports: %d", totalCount, validCount)
}

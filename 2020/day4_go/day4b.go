package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
)

func parsePassportsLines(dat string) []string {
	lines := regexp.MustCompile("\r?\n ?\r?\n").Split(dat, -1)

	return lines
}

func parsePassport(passport string) map[string]string {
	passportMap := map[string]string{}

	for _, keyval := range regexp.MustCompile("[\\s\r\n]").Split(passport, -1) {
		matches := regexp.MustCompile("(?i)([a-z]+):(.*)").FindAllStringSubmatch(keyval, 1)
		if len(matches) > 0 {
			passportMap[matches[0][1]] = matches[0][2]
		}
	}

	return passportMap
}

func stringInMap(m map[string]string, key string) bool {
	_, ok := m[key]
	return ok
}

func parseHeight(value string) (int, string, error) {
	matches := regexp.MustCompile("(\\d+)(cm|in)").FindAllStringSubmatch(value, 1)
	if len(matches) > 0 {
		height, err := strconv.Atoi(matches[0][1])
		return height, matches[0][2], err
	}
	return 0, "", errors.New("not valid height")
}

func checkPassportIsValid(passport string) bool {

	passportParsed := parsePassport(passport)

	if stringInMap(passportParsed, "byr") && stringInMap(passportParsed, "iyr") && stringInMap(passportParsed, "eyr") && stringInMap(passportParsed, "hgt") && stringInMap(passportParsed, "hcl") && stringInMap(passportParsed, "ecl") && stringInMap(passportParsed, "pid") {
		byr, _ := strconv.Atoi(passportParsed["byr"])
		iyr, _ := strconv.Atoi(passportParsed["iyr"])
		eyr, _ := strconv.Atoi(passportParsed["eyr"])
		hgt, hgtunit, _ := parseHeight(passportParsed["hgt"])
		hcl := regexp.MustCompile("^#[0-9a-f]{6}$").MatchString(passportParsed["hcl"])
		ecl := regexp.MustCompile("^(amb|blu|brn|gry|grn|hzl|oth)$").MatchString(passportParsed["ecl"])
		pid := regexp.MustCompile("^[0-9]{9}$").MatchString(passportParsed["pid"])

		if hcl && ecl && pid && byr >= 1920 && byr <= 2002 && iyr >= 2010 && iyr <= 2020 && eyr >= 2020 && eyr <= 2030 && ((hgtunit == "cm" && hgt >= 150 && hgt <= 193) || (hgtunit == "in" && hgt >= 59 && hgt <= 76)) {
			return true
		}
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

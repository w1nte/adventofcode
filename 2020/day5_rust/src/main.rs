
use std::io::{self, BufRead};

fn calc_seat_by_boarding(boarding: &str, num: i32, rows: i32) -> i32 {
    let first_character = boarding.chars().nth(0).unwrap();
    let next_rows: i32 = rows / 2;
    let mut next_num = num;

    if first_character == 'B' || first_character == 'R' {
        next_num += next_rows
    }

    if boarding.chars().count() == 1 {
        return next_num;
    }

    calc_seat_by_boarding(&boarding[1..], next_num, next_rows)
}

fn calculate_seat_col(boarding: &str) -> i32 {
    calc_seat_by_boarding(&boarding[7..10], 0, 8)
}

fn calculate_seat_row(boarding: &str) -> i32 {
    calc_seat_by_boarding(&boarding[0..7], 0, 128)
}

fn calculcate_seat(boarding: &str) -> i32 {
    let row = calculate_seat_row(boarding);
    let col = calculate_seat_col(boarding);

    row * 8 + col
}

fn main() {
    let mut highest_seat_number = 0;
    let mut seat_numbers = Vec::new();

    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let input = &String::from(line.unwrap());
        if input.chars().count() == 10 {
            let seat_number = calculcate_seat(input);
            seat_numbers.push(seat_number);

            if seat_number > highest_seat_number {
                highest_seat_number = seat_number
            }

            println!("Seat ID: {}", seat_number);
        } else {
            break;
        }
    }

    seat_numbers.sort();
    let mut prev_seat: i32 = 0;
    for seat_id in seat_numbers {
        if prev_seat == seat_id - 2 {
            println!("My seat ID: {}", seat_id - 1);
        }

        prev_seat = seat_id;
    }
    
    println!("Highest seat ID: {}", highest_seat_number);
}

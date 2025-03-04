fn check_powers_of_three(mut n: i32) -> bool {
    while n > 0 {
        if n % 3 == 2 {
            return false;
        }
        n /= 3;
    }
    true
}

fn main() {
    let n = 12;
    println!("{}", check_powers_of_three(n));
}
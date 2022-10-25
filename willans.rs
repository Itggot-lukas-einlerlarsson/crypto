use std::f64::consts::PI;

/// willans nth prime formulae -- absurd time complexity but still interesting
pub fn nth_prime(nth_prime : i64) -> f64 {
    let mut count : i64 = 1;
    let mut prime_sum : f64 = 0.0;
    let range : i64 = 2_i64.pow(nth_prime as u32);
    while count <  range {
        prime_sum += (nth_prime as f64/num_of_primes(count) as f64).powf(1.0/nth_prime as f64).floor();
        count += 1;
    }
    prime_sum //after input: 7 fail, fail in prime checker
}

/// returns 1 if number is prime, 0 if number is composite.
pub fn prime_checker(number : f64) -> i8 {
    let factor : f64 =  ((factorial(number-1.0)+1.0)/number) as f64;
    let mut product : f64 = (PI*factor).cos().powf(2.0); // <--- problemo,
    // product doesnt become 1.0 after the prime 17 as it should cuz of float imprecision
    let check : f64 = product.floor();
    check as i8
}

/// number of primes <= max_value+1
pub fn num_of_primes(max_value : i64) -> i64 {
    let mut number : i64 = 1;
    let mut count : i64 = 1;
    while number < max_value {
        if prime_checker(number as f64) == 1 {
            count += 1;
        }
        number += 1;
    }
    count //count represents number of primes.
}

pub fn factorial(mut num : f64) -> f64 {
    let mut product : f64 = 1.0;
    while num > 1.0 {
        product *= num;
        num -= 1.0;
    }
    product
}

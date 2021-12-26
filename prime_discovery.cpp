/*
  Just an idea, will maybe come back and try to finish.
  this program tries to predict primes via patterns of previous primes.
index has a relation to the prime? previous primes has relation to future prime ?
some previous primes can be multiplied by two and then futher previous primes can be added/subtracted to find future primes futher down the line?
ex maybe there is a pattern here:
patterns based on primeintervals who's numbers gets multiplied by 2 or +/- to get a prime futher down the line?
1             1 = 1
2             2 = 2 * 1
3             3 = 2 * 1 + 1, 2 * 2 -1
4             5 = 2 * 2 + 1, 2 * 3 -1
5             7 = 2 * 3 + 1, 2 * 5 -3
6           11 = 2 * 5 + 1, 2 * 7 -3
7           13 = 2 * 5 + 3, 2 * 7 - 1
8           17 = 2 * 7 + 3, 2 * 11 - 5
9           19 = 2 * 7 + 5, 2* 11 - 3
10         23 = 2 * 11 + 2, 2 * 13 - 3
11         29 = 2 * 13 + 3, 2 * 17 - 5
12         31 = 2 * 13 + 5, 2 * 17 - 3
13         37 = 2 * 17 + 3, 2 * 19 - 1
14         41 = 2 * 19 + 5, 2 * 23 -5
15         43 = 2 * 19 + 7, 2 * 23 - 3
16         47 = 2 * 23 + 1, 2 * 29 - 11
17         53 = 2 * 23 + 7, 2 * 29 - 5
18         59 = 2 * 29 + 1, 2 * 31 - 3
19         61 = 2 * 29 + 3, 2 * 31 - 1
20         67 = 2 * 31 + 5, 2 * 37 - 7
21         71 = 2 * 29 + 13, 2 * 37  - 3, 2 * 41 - 11
22         73 = 2 * 31 + 11, 2 * 37 -1
23         79 = 2 * 37 + 5, 2 * 41 - 3
24         83 = 2 * 41 + 1, 2 * 43 - 3
25         89 = 2 * 43 + 3, 2 * 47 - 5
26         97 = 2 *  47 + 3, 2 * 43 + 11
27         101 = 2 * 47 + 7, 2 * 53 - 5
*/

#include <iostream>
#include <string>
#include <vector>
#include <cmath>

void printPrimeVector(const std::vector<int> &primeVector);
void getPrimeVector(std::vector<int> &primeVector, const int& max);
std::string getVectorPatterns(const std::vector<int> &primeVector, int max); //check to see if primes before *2 +- other primes before get present prime
void predictPrime(const std::vector<int> &primeVector);
// ev: bool isPrime(const std::vector<int> &primeVector)

int main(int argc, char const *argv[]) {
  std::vector<int> primeVector = {1, 2, 3, 5}; //vector used to check primes
  const int MAX_PRIME = 5000; //all primes less than 5000 is being checked.
  getPrimeVector(primeVector, MAX_PRIME);
  printPrimeVector(primeVector);
  //std::vector<int> primePredictVector = {1, 2, 3, 5}; //vector used to predict primes
  return 0;
}

std::string getVectorPatterns(const std::vector<int> &primeVector){
  //trying to find intervals appropriate to multiply and add/subtract to predict prime
  int middleBoundPrime = primeVector.size()/2+1;
  if (primeVector[primeVector.size()/2]+1 > primeVector[primeVector.size()-1]) {
    int middleBoundPrime = primeVector.size()/2;
  } else {
    int middleBoundPrime = primeVector.size()/2;
  }
  int lowerBoundPrime = primeVector.size()/4;
  std::string primePattern;
  return primePattern;
}

void printPrimeVector(const std::vector<int> &primeVector) {
  for (size_t i = 0; i < primeVector.size(); i++) {
    std::cout << primeVector[i] << '\t';
  }
  std::cout << '\n';
}

void getPrimeVector(std::vector<int> &primeVector, const int& max){
  bool prime = true;
  for (size_t i = 6; i < max; i++) {
    prime = true;
    for (size_t j = 1; j < primeVector.size(); j++) {
      if (i % primeVector[j] == 0) {
        prime = false;
      }
    }
    if (prime == true) {
      primeVector.push_back(i);
    }
  }
}

//a^2 = (a-1)(a+1)+1

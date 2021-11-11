#include <iostream>
#include <string>
#include <algorithm>
#include <exception>
#include <string>

void userHandler();
void encrypt(std::string& text, int a, int b);
void decrypt(std::string& text, int a, int b); // c = inv(a) % 26 and d = -inv(a)*b % 26
void capitalize(std::string& string); // checks input, each letter -> capital letter
int oldModInverse(int a, int b);
int modInverse(int a);


int main(int argc, char const *argv[]) {
  userHandler();
  return 0;
}

void userHandler(){
  std::string text; //= "the laundromat is a front"
  int a, b;
  int choice;
  std::cout << "only decipher(1) or both cipher and decipher(2)?" << '\n';
  std::cin >> choice;
  std::cin.ignore();
  if (choice < 1 || choice > 2) {
    std::cout << "bad input." << '\n';
    exit(1);
  }
  std::cout << "indata: " << ' ';
  std::getline(std::cin, text);
  std::cout << "with key:" << '\n' << "a: ";
  std::cin >> a;
  std::cin.ignore();
  std::cout << "b: ";
  std::cin >> b;
  if (choice == 2) {
    capitalize(text);
    std::cout << "Plaintext: " << text << '\n';
    encrypt(text, a, b);
    std::cout << "Ciphertext: " <<text << '\n';
    decrypt(text, a, b);
    std::cout << "Plaintext': " << text << '\n';
  } else {
    capitalize(text);
    decrypt(text, a, b);
    std::cout << "Plaintext': " << text << '\n';
  }
}

int modInverse(int a){ //bruteforce modInverse
  a = a % 26;
  for (size_t i = 1; i < 27; i++) {
    if ((a*i) % 26 == 1) {
      std::cout << i << '\n';
      return i;
    }
  }
  return 21;
}

void encrypt(std::string& text, int a, int b){
  char temp;
  for (size_t i = 0; i < text.length(); i++) {
    if (text[i] == ' ') {
      continue;
    }
    temp = (a * (text[i]-65) + b )% 26;
    text[i] = temp + 65;
  }
}

void decrypt(std::string& text, int a, int b){
  char temp;
  int c = modInverse(a), d = -c*b%26;
  if (c == 1) {
    std::cout << "No solution exists?" << '\n';
    return;
  }
  if (d < 0) {
    d += 26;
  }
  std::cout << "c: " << c << "\tand d: " << d << '\n';
  for (size_t i = 0; i < text.length(); i++) {
    if (text[i] == ' ') {
      continue;
    }
    temp = (c * (text[i]-65) + d )% 26;
    text[i] = temp + 65;
  }
}

void capitalize(std::string& string)
{
  char temp;
  for (size_t i = 0; i < string.length(); i++)
  {
    if (!(string[i] >= 'A' && string[i] <= 'Z') && !(string[i] >= 'a' && string[i] <= 'z') && string[i] != ' ')
    {
      std::string error = "Not only letters and spaces used in input.";
      throw std::runtime_error(error);
    }
    if (string.length() < 3)
    {
      std::string error = "string to short.";
      throw std::runtime_error(error);
    }
    if (string[i] >= 'a' && string[i] <= 'z')
    {
      temp = string[i];
      temp -= 32;
      string[i] = temp;
    }
  }
}

int oldModInverse(int a, int b){ // b = 26
  //using extended euclidian https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
  int t = 0, new_t = 1;
  int r = b, new_r = a;
  int qoutient = 0;
  int temp;
  while (new_r != 0) {
    qoutient = r/new_r % 26;
    temp = r;
    r = new_r;
    new_r = temp - qoutient * new_r;

    //and
    temp = t;
    t = new_t;
    new_t = temp - qoutient*new_t;
  }
  if (t <0) {
    t = t+b;
  }
  return t;
}

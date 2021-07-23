#include <iostream>
#include <string>
#include <exception>

//functional programming

void capitalize(std::string& string);
std::string encipher(std::string& text, const int key);
std::string decipher(std::string& text, const int key); //find key and dechiper

int main(int argc, char const *argv[])
{
  //only capital letters
  std::string text;
  int key;
  std::cout << "Put in text to be encrypted: " << ' ';
  std::getline(std::cin, text);
  capitalize(text);
  std::cout << "With what key? " << ' ';
  std::cin >> key;
  if (key < 0 || key > 27)
  {
    std::string error = "invalid key.";
    throw std::runtime_error(error);
  }
  std::cout << "Plain Text: " << text << '\n';
  text = encipher(text, key);
  std::cout << "Enciphered Text: " << text << '\n';
  text = decipher(text, key);
  std::cout << "Deciphered Text: "  << text<< '\n';
  return 0;
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
    if (string[i] >= 'a'&& string[i] <= 'z')
    {
      temp = string[i];
      temp -= 32;
      string[i] = temp;
    }
  }
}

std::string encipher(std::string& text, const int key)
{
  char temp;
  int mod;
  for (size_t i = 0; i < text.length(); i++)
  {
    temp = text[i];
    temp += key;
    if (temp > 'Z')
    {
      mod = temp % 91;
      temp = 'A' + mod;
    }
    if (temp < 'A')
    {
      continue; //skips to next iteration
    }
    text.at(i) = temp;
  }
  return text;
}

std::string decipher(std::string& text, const int key)
{
  //std::string bruh; // later used for unknwn key chekc
  char temp;
  int mod;
  for (size_t i = 0; i < text.length(); i++)
  {
    temp = text[i];
    temp -= key;
    if (temp < 'A')
    {
      mod = 64 - temp; //65 = 'A'
      temp = 'Z' - mod;
    }
    if (temp < 'A')
    {
      temp = ' '; //skips to next iteration
    }
    text.at(i) = temp;
  }
  return text;
}

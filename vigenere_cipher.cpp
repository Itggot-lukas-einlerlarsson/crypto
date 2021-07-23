#include <iostream>
#include <string>
#include <exception>
#include <iomanip>

//*vigenere not virgenere :), whatever

class Virgenere
{
private:
  int alphabetSize;
  char* alphabet;
  char** table;
  std::string text;
  std::string key;
  std::string keystream;

public:

  // inits / dels
  Virgenere ();
  ~Virgenere ();

  //class functions
  void printTable();
  void printAlphabet();
  void capitalize(std::string& string);
  void userHandler();
  int letterVal(const char& letter);
  void createKeystream();
  void encipher();
  void decipher();

};

Virgenere::Virgenere ()
: alphabetSize(26), alphabet(new char[alphabetSize]), table(new char*[alphabetSize])
{
  char letter = 'A';
  for (size_t i = 0; i < alphabetSize; i++)
  {
    alphabet[i] = letter;
    letter++;
  }
  letter = '@';
  int mod;
  for (size_t i = 0; i < alphabetSize; i++)
  {
    letter++;
    table[i] = new char[alphabetSize];
    for (size_t j = 0; j < alphabetSize; j++)
    {
      if (letter > 'Z')
      {
        mod = letter % 91;
        letter = 'A' + mod;
      }
      table[i][j] = letter;
      letter++;
    }
  }
}

Virgenere::~Virgenere ()
{
  delete [] alphabet;
  for (size_t i = 0; i < alphabetSize; i++)
  {
    delete [] table[i];
  }
  delete [] table;
}

void Virgenere::printAlphabet()
{
  for (size_t i = 0; i < alphabetSize; i++)
  {
    std::cout << alphabet[i] << ' ';
  }
  std::cout << '\n';
}

void Virgenere::printTable()
{
  std::cout << "Hello and welcome to a beautiful session of cryptography!" << '\n';
  std::cout << "0 | ";
  printAlphabet();
  std::cout << std::setfill('_') << std::setw(56) << '\n';
  for (size_t i = 0; i < alphabetSize; i++)
  {
    std::cout << table[i][0] << " | ";
    for (size_t j = 0; j < alphabetSize; j++)
    {
      std::cout << table[i][j] << ' ';
    }
    std::cout << '\n';
  }
}

void Virgenere::capitalize(std::string& string)
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
    if (string[i] >= 'a'&& string[i] <= 'z')
    {
      temp = string[i];
      temp -= 32;
      string[i] = temp;
    }
  }
}

void Virgenere::userHandler()
{
  printTable();
  std::cout << "What text do ya want to encrypt?" << ' ';
  std::getline(std::cin, text);
  capitalize(text);
  std::cout << "With what key(key needs to be longer than two characters)?" << ' ';
  std::cin >> key;
  capitalize(key);
  //fix if key is digit or is less than three characters...
  createKeystream();
  std::cout << "Keystream: " << keystream << '\n';
  std::cout << "Plaintext: " << text <<'\n';
  encipher();
  std::cout << "Ciphertext: " << text <<'\n';
  decipher();
  std::cout << "Deciphertext: " << text <<'\n';
}

int Virgenere::letterVal(const char& letter)
{
  int value = letter - 65;
  return value;
}

void Virgenere::createKeystream()
{
  for (size_t i = 0, j = 0; i < text.length(); i++, ++j)
  {
    if (j == key.length())
    {
      j = 0;
    }
    keystream += key[j]; // ev
  }
}

void Virgenere::encipher()
{
  for (size_t i = 0; i < text.length(); i++)
  {
    if (text[i] < 'A') //if space
    {
      continue; //skips to next iteration
    }
    text[i] = table[letterVal(keystream[i])] [letterVal(text[i])];
  }
}

void Virgenere::decipher()
{ //reverse
  int index;
  for (size_t i = 0; i < text.length(); i++)
  {
    if (text[i] < 'A') //if space
    {
      text[i] = ' ';
      continue; //skips to next iteration
    }
    for (size_t j = 0; j < alphabetSize; j++)
    {
      if (table[letterVal(keystream[i])][j] == text[i])
      {
        index = j;
        break;
      }
    }
    text[i] = table[0] [index];
  }
}


int main(int argc, char const *argv[])
{
  Virgenere crypt;
  crypt.userHandler();
  return 0;
}

// random.cpp: Parag Amrutkar
// Description: Random number game

#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

int main() {
  int secret_number, guess_number;
  srand (time(NULL));
  secret_number = rand() % 100 + 1;

  cout << "Guess our number (1 to 100)" << endl;
  do {
    if (!(cin >> guess_number)) {
      cout << "Please enter a numeric value.";
      cin.clear();
      cin.ignore(1000, '\n');
      continue;
    } else {
      if (guess_number < secret_number) cout << "The secret number is higher than " << guess_number << endl;
      else if (guess_number > secret_number) cout << "The secret number is lower than " << guess_number << endl;
    }
  } while (guess_number != secret_number);
  cout << "You guessed it right! It is " << secret_number << endl;
}

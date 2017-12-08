#include <iostream>
using namespace std;

int getInput() {
  cout << "Enter a three digit number: ";
  int number;
  if(!(cin >> number)) {
    cout << "Enter numerical value!" << endl;
    return -1;
  }
  if (!(number >= 100 && number < 1000)) {
    cout << "Enter three digit numerical value!" << endl;
    return -1;
  }
  return number;
}

int main() {
  int number, temp;
  if((number = getInput()) == -1) return 0;

  // Save the digits in an array
  int digits[3];
  temp = number;
  for (int i = 2; i >= 0; i--) {
    digits[i] = temp%10;
    temp /= 10;
  }
  // cout << "Digits in the number are: " << endl;
  // for(int i = 0; i < 3; i++) cout << digits[i] << endl;
  // cout << endl;

  // Store 3 3-digit numbers formed by the the digits
  int numberCombinations[3] = {0};
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      numberCombinations[i] = numberCombinations[i]*10 + digits[(i+j)%3];
    }
    numberCombinations[i] %= 11;
    // cout << numberCombinations[i] << endl;
  }
  // cout << endl;

  temp = numberCombinations[0];
  numberCombinations[0] += numberCombinations[1];
  numberCombinations[1] += numberCombinations[2];
  numberCombinations[2] += temp;

  // for(int i = 0; i < 3; i++) cout << numberCombinations[i] << endl;
  // cout << endl;

  for(int i = 0; i < 3; i++) {
    if(numberCombinations[i]%2 != 0) {
      temp = numberCombinations[i];
      if(!((numberCombinations[i] -= 11) >= 0)) numberCombinations[i] = temp+11;
      if(numberCombinations[i] == 9) cout << "Alert!! Sum is 9!" << endl;
    }
    numberCombinations[i] /= 2;
    cout << numberCombinations[i] << endl;
  }

  return 0;
}

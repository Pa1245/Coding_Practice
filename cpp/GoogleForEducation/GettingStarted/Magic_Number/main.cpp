#include <iostream>
using namespace std;

int getInput() {
  cout << "Enter a three digit number whose 1st digit is greater than third digit: ";
  int number;
  if(!(cin >> number)) {
    cout << "Enter numerical value!" << endl;
    return -1;
  }
  if (!(number >= 100 && number < 1000)) {
    cout << "Enter three digit numerical value!" << endl;
    return -1;
  }
  if (!(number/100 > number%10)) {
    cout << "First digit should be greater than third!" << endl;
    return -1;
  }
  return number;
}

int reverse(int n) {
  int temp = 0;
  while (n != 0) {
    temp = temp*10 + n%10;
    n /= 10;
  }
  return temp;
}

int main() {
  int number;
  if((number = getInput()) == -1) return 0;
  else cout << "input number: " << number << endl;
  int revNumber = reverse(number);
  cout << "reverse it: " << revNumber << endl;
  int subtractNumber = number - revNumber;
  cout << "subtract: " << subtractNumber << endl;
  cout << "reverse it: " << reverse(subtractNumber) << endl;
  cout << "add: " << subtractNumber << " + " << reverse(subtractNumber) << " = " <<
    subtractNumber+reverse(subtractNumber) << endl;
  return(0);
}

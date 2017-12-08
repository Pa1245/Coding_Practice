// get_input.cpp: Parag Amrutkar
// Description: Learn to use cin to get input.

#include <iostream>
using namespace std;

int main() {
  int input_var = 0;
  do {
    cout << "Enter a numnber (-1 = quit): ";
    if (!(cin >> input_var)) {
      // cout << "You entered a non-numeric. Exiting.." << endl;
      // break;
      cout << "You entered a non-numeric. Please enter a numeric value." << endl;
      cin.clear();
      cin.ignore(1000, '\n');
      continue;
    }
    if (input_var != -1) {
      cout << "You entered " << input_var << endl;
    }
  } while (input_var != -1);
  cout << "All done." << endl;
  return 0;
}

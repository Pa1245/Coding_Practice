#include <iostream>
using namespace std;

int main() {
  string Months[] = {"January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"};
  cout << "Enter the code for expiry date of product: ";
  string code;
  cin >> code;
  int month = code[0]-'A'+1;
  int date = (code[1]-'Q'+1)*10 + (code[2]-'Q'+1);
  int year = code[3]-'A'+1 + 1995;
  cout << date << " " << Months[month] << ", " << year << endl;
  return 0;
}

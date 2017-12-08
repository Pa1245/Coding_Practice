#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
  int gcd(int a, int b);
  int a, b;
  cout << "Enter two integers: ";
  if (!(cin >> a >> b)) {
    cout << "Please enter only integers" << endl;
  } else {
    cout << "GCD of " << a << " and " << b << " is " << gcd(a, b) << endl;
  }
  return 0;
}

int gcd(int a, int b) {
  int temp;
  while (b != 0) {
    temp = a % b;
    a = b;
    b = temp;
  }
  return a;
}

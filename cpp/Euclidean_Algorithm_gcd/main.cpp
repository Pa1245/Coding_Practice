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
    cout << "GCD of " << a << " and " << b << " is " << gcd(abs(a), abs(b)) << endl;
  }
  return 0;
}

int gcd(int a, int b) {
  while(true) {
    if (a == 0) return b;
    else if (b == 0) return a;
    else {
      int temp = b;
      if (a > b) {
        b = a%b;
        a = temp;
      } else {
        b = a;
        a = temp%a;
      }
    }
  }
}

#include <iostream>
using namespace std;

void printF() {
  cout << "FFFFF\nF\nFFF\nF\nF" << endl;
}

void printE() {
  for(int i = 0; i < 5; i++) {
    if(i%2 == 0) cout << string(5, 'E') << endl;
    else cout << 'E' << endl;
  }
}

int main() {
  printE();
  return 0;
}

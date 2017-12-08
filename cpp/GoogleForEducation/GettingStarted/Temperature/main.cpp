#include <iostream>
using namespace std;

int GetInput() {
  int chirps = 0;
  cout << "Enter the number of chirps: ";
  if(!(cin >> chirps)) {
    cout << "Only numbers" << endl;
    return 0;
  }
  return chirps;
}

void CalcTemp(int Chirps) {
  cout << "Temperature: " << Chirps/4 + 10 << endl;
}

int main() {
  int numberOfChirps = GetInput();
  CalcTemp(numberOfChirps);
}

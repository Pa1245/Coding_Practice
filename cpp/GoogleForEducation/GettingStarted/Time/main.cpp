#include <iostream>
using namespace std;

int GetInput(string message) {
  int value;
  cout << message << ": ";
  if(!(cin >> value)) {
    cout << "Only numbers!" << endl;
    return 0;
  }
  return value;
}

void TimeInHMS(int Seconds) {
  int h = Seconds/3600;
  int m = (Seconds%3600)/60;
  int s = (Seconds%3600)%60;
  cout << "Hours: " << h << endl << "Minutes: " << m << endl << "Seconds: " << s << endl;
}

int main() {
  int timeInSeconds = GetInput("Number of seconds");
  TimeInHMS(timeInSeconds);
  return 0;
}

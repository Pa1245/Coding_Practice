// Weekly_Earnings/main.cpp, Parag Amrutkar
// Description: A program to decide the beset of three methods of compensation

#include <iostream>
using namespace std;

// constants which are used throughout the program
#define kPricePerUnit 225
#define kWeeklyWage 600
#define kSalary 7.0
#define kHoursPerWeek 40
#define kCommission2 0.10
#define kCommision3 0.20
#define kBonusPerUnit 20

int GetInput() {
  std::cout << "Enter number of units sold per week: ";
  int units = 0;

  if(!(std::cin >> units)) {
    cout << "Numbers Only" << endl;
  }
  return units;
}

void CalcMethod1() {
  cout << "Method 1: " << kWeeklyWage << endl;
}

void CalcMethod2(int Sales) {
  cout << "Method 2: " << kSalary*kHoursPerWeek + 0.1*Sales*kPricePerUnit << endl;
}

void CalcMethod3(int Sales) {
  cout << "Method 3: " << (0.1*kPricePerUnit + 20)*Sales << endl;
}

int main(void) {
  int WeeklySales = GetInput();
  if (WeeklySales == 0) return 0;
  CalcMethod1();
  CalcMethod2(WeeklySales);
  CalcMethod3(WeeklySales);
  return 0;
}

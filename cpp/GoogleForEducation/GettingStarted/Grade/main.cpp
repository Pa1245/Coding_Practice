#include <iostream>
using namespace std;

float GetInput(string message) {
  int value = 0;
  cout << "Enter the score for the " << message << ": ";
  if (!(cin >> value)) {
    cout << "Enter intergers only.";
    return 0;
  }
  return value;
}

int PrintFinalGrade() {
  float assignmentGrade = 0, midtermGrade = 0,
    finalExaminationGrade = 0, classParticipationGrade = 0;
  for(int i = 1; i <= 4; i++) {
    switch (i) {
      case 1:
        assignmentGrade += GetInput("first assignment");
        break;
      case 2:
        assignmentGrade += GetInput("second assignment");
        break;
      case 3:
        assignmentGrade += GetInput("third assignment");
        break;
      case 4:
        assignmentGrade += GetInput("fourth assignment");
        break;
    }
  }
  midtermGrade = GetInput("midterm");
  finalExaminationGrade = GetInput("final");
  classParticipationGrade = GetInput("section grade");

  cout << "The final grade is: " << assignmentGrade*0.4/4 + midtermGrade*0.15
    + finalExaminationGrade*0.35 + classParticipationGrade*0.1 << endl;
}

int main() {
  PrintFinalGrade();
  return 0;
}

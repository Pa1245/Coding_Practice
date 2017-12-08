// file.cpp, Parag Amrutkar
// Description: Learing file processing

#include <iostream>
#include <fstream>
using namespace std;

int main() {
  char first_name[30], last_name[30]; int age;
  char file_name[20];
  // Collect the data

  cout << endl << "Enter the name of the file: "; cin >> file_name;

  // Create an ofstream called People, open the stream for output
  ofstream People(file_name, ios::out);
  char done;
  while (1) {
    cout << endl << "Enter the first Name: "; cin >> first_name;
    cout << "Enter the Last Name: "; cin >> last_name;
    cout << "Enter Age: "; cin >> age;

    // Write the output to the stream.
    People << first_name << endl << last_name << endl << age << endl;
    
    cout << "Continue(y/n)? ";
    cin >> done;
    if(done == 'n') break;
  }

  People.close();

  ifstream inFile(file_name);
  if(!inFile) {
    cout << "Unable to open file"<< endl;
    return 1;
  }
  while (1) {
    inFile >> first_name >> last_name >> age;
    if (inFile.eof()) break;
    cout << endl << "First Name: " << first_name;
    cout << endl << "Last Name:  " << last_name;
    cout << endl << "Enter Age:  " << age;
    cout << endl;
  }

  inFile.close();
  return 0;
}

#include <iostream>
#include <iomanip>
using namespace std;

int main () {

  for (int r = 0; r < 100; r++)
    for (int p = 0; p < 100; p++)
      for (int h = 0; h < 100; h++)
        if (r + p + h == 100)
          if (r*0.5 + p*3 + h*10 == 100)
            cout << "Horses: " << setw(3) << h << "\tPigs: " << setw(3) << p << "\tRabbits: " << setw(3) << r << endl;
}

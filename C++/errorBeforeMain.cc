#include <iostream>
#include "stdlib.h"

class Thing {

public:
  Thing(int x) {
    std::cout << "error " << x << std::endl;
    exit(x);
  }
private:
  Thing() {

  }
};

Thing t(4);
int main() {
  std::cout << "main" << std::endl;
}

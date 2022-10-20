#include <iostream>
using namespace std;

int main() {
    int temp, i = 1, j = 2, sum = 0;
    while (i <= 4000000) {
        if (i % 2 == 0)
            sum += i;
        temp = i + j;
        i = j;
        j = temp;
    }
    cout << sum << "\n";
    return 0;
}
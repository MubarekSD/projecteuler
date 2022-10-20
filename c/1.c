#include <stdio.h>

int main(void) {
    int temp, i = 1, j = 2, sum = 0;
    while (i <= 4000000) {
        if (i % 2 == 0)
            sum += i;
        temp = i + j;
        i = j;
        j = temp;
    }
    printf("%d\n", sum);
    return (0);
}
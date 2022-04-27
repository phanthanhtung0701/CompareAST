#include <stdio>

int func1(int n){
    int sum = 0;
    int i = 0;
    do {
        sum = sum + i;
        i++;
    }
    while (i < n-1);
    return sum;
}
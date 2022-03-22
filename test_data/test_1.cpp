#include <iostream>

//using namespace std;

int main()
{
    int a=10, b=9;
    while(b!=0) {
        if (a>b) {
            a = a-b;
        }
        else {
            b = b - a;
        }
    }
}

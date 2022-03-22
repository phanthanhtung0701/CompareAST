#include <iostream>

//using namespace std;

int main()
{
    int c=10, d=9;
    while(c!=0) {
        if (c>d) {
            c = c - d;
        }
        else {
            d = d - c;
        }
    }
}

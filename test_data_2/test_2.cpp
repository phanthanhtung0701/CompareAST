#include <iostream>

//using namespace std;
int b = 0;
char c = "b";
char city[7];
int *c = 0;
int main()
{
    int c=10, d=9, e = 10;
    while(c!=0) {
        if (c>d) {
            c = c - d;
        }
        else {
            d = d - c;
        }
    }
    return c+d;
}

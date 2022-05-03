#include<iostream>
using namespace std;
int n,a[1000];
bool ok;
void sinh()
{
    int i = n;
    while(i > 0 && a[i] == 1)
    {
        a[i] = 0;
        i--;
    }
    if(i == 0) ok = false;
    else a[i] = 1;
}
bool check()
{
    for(int i = 1; i <= n/2; i++)
    {
        if(a[i] != a[n-i+1]) return false;
    }
    return true;
}
int main()
{
    cin >> n;
    ok = true;
    for(int i = 1; i <= n; i++) a[i]=0;
    while(ok)
    {
        if(check())
        {
            for(int i = 1; i <= n; i++) cout << a[i] << " ";
            cout << endl;
        }
        sinh();
    }
}
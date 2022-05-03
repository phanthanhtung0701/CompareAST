#include <iostream>
using namespace std;
int t, n, a[100];
bool check() {
    for(int i = 1; i <= n / 2; i++) {
        if(a[i] != a[n - i + 1]) return false;
    }
    return true;
}
void result() {
    for(int i = 1; i <= n; i++) cout << a[i] << " ";
    cout << endl;
}
void Try(int i) {   
    for(int j = 0; j <= 1; j++) {
        a[i] = j;
        if(i == n) {
            if(check()) result();
        }
        else Try(i + 1);
    }
}
main() {
    cin >> n;
    Try(1);
    return 0;
}
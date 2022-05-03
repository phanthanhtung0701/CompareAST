#include <bits/stdc++.h>
using namespace std;
int a[20], n;

bool check() {
    for(int i = 1; i <= n; i++) {
        if(a[i] != a[n - i + 1]) return false;
    }
    return true;
}

void Try(int i) {
    for(int j = 0; j <= 1; j++) {
        a[i] = j;
        if(i == n) {
            if(check()) {
                for(int i = 1; i <= n; i++) {
                    cout << a[i] << "\t";
                }
                cout << endl;
            }
        }
        else Try(i + 1);
    }
}

int main() {
    cin >> n;
    Try(1);
}
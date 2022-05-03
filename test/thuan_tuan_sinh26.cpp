#include <bits/stdc++.h>
using namespace std;

int n, a[1001];

void in(int a[], int n) {
	for (int i = 1; i <= n; ++i) {
		cout << a[i] << " ";
	}
	cout << endl;
}

int check() {
	for (int i = 1; i <= n; i++) {
		if (a[i] != a[n - i + 1]) return 0;
	}
	return 1;
}

void sinh() {
	for (int i = 1; i <= n; ++i) a[i] = 0;
	int ok = 1;
	while (ok) {
		if (check()) in(a, n);
		int i = n;
		while (i >= 1 && a[i] == 1) {
			a[i] = 0;
			--i;
		}
		if (i == 0) ok = 0;
		else a[i] = 1;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> n;
	sinh();
}
#include<iostream>
using namespace std;
int n;
int arr[25];
int check() {
	int x[25];
	int cnt = 0;
	for (int i = n - 1; i >= 0; i--) {
		x[cnt] = arr[i];
		cnt++;
	}
	for (int i = 0; i < n; i++) {
		if (x[i] != arr[i]) {
			return 0;
		}
	}
	return 1;
}
void dequy(int i) {
	if (i == n) {
		if(check()){
			for (int i = 0; i < n; i++) {
				cout << arr[i] << " ";
			}
			cout << endl;
		}
		return;
	}
	arr[i] = 0;
	dequy(i + 1);
	arr[i] = 1;
	dequy(i + 1);
}
int main() {
	cin >> n;
	dequy(0);
}
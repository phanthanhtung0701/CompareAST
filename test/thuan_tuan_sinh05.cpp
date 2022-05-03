#include<bits/stdc++.h>
using namespace std;
int kt(int a[], int n){
	int l = 0, r = n - 1;
	while (l<r){
		if (a[l] != a[r]) return 0;
		l++; r--;
	}
	return 1;
}
void sinh(int a[], int n, int &ok){
	if (kt(a, n)){
		for (int i=0;i<n;i++) cout<<a[i]<<" ";
		cout<<endl;
	}
	int i = n-1;
	while (i >= 0 && a[i] == 1){
		a[i] = 0; i--;
	}
	if (i < 0) ok = 0;
	else a[i] = 1;
}
main(){
	int n; cin>>n;
	int a[n];
	for (int i=0;i<n;i++) a[i] = 0;
	int  ok = 1;
	while (ok == 1){
		sinh(a, n, ok);}
}

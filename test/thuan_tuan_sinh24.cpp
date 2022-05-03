#include<bits/stdc++.h>
using namespace std;
int n, a[1001];
void check(){
	int l=1, r=n;
	while(l < r){
		if(a[l]!=a[r]){
			return;
		}
		l++;
	    r--;
	} 
	for(int i=1; i <= n; i++)
		cout << a[i] << " ";
	cout << endl;
}
void sinh(int i){
	for(int j=0; j <= 1; j++){
		a[i]=j;
		if(i==n)
		check();
		else sinh(i+1);
	}
}
int main(){
	cin >> n;
	sinh(1);
	return 0;
}
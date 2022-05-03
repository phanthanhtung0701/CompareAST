#include<bits/stdc++.h>
using namespace std;
int n,a[1001];
void inkq(){
	bool ok=true;
	for(int i=1;i<=n/2;i++){
		if(a[i] != a[n-i+1]){
			ok=false;
			break;
		}
	}
	if(ok){
		for(int i=1;i<=n;i++){
			cout<<a[i]<<" ";
		}
		cout<<endl;
	}
}
void ql(int i){
	for(int j=0;j<=1;j++){
		a[i]=j;
		if(i==n){
			inkq();
		}
		else ql(i+1);
	}
}
int main(){
	cin>>n;
	ql(1);
}
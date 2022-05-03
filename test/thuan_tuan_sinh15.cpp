#include<bits/stdc++.h>

using namespace std;
int n,a[100];
bool check1(){
	for(int i=1;i<=n;i++){
		if(a[i]==0){
			return true;
		}
	}
	return false;
}

bool check2(){
	for(int i=1;i<=n/2;i++){
		if(a[i]!=a[n-i+1]){
			return false;
		}
	}
	return true;
}
void sinh(){
	for(int i=n;i>=1;i--){
		if(a[i]==0){
			a[i]=1;
			break;
		}
		else
			a[i]=0;
	}
	if(check2()){
		for(int i=1;i<=n;i++){
			cout<<a[i]<<"\t";
		}
		cout<<endl;
	}
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		a[i]=0;
		cout<<a[i]<<"\t";
	}
	cout<<endl;
	while(check1()){
		sinh();
	}
	return 0;
}
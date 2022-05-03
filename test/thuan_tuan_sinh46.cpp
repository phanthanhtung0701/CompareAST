#include<iostream>
using namespace std;
void Xaudautien(int n, int a[]){
	for(int i=0; i<n; i++){
		a[i]=0;
	}
}
void Xuat( int n, int a[]){
	int dem=0;
	for(int i=0; i<n/2; i++){
		if(a[i]==a[n-1-i]){
			dem++;
		}
	}
	if(dem==n/2){
		for(int i=0; i<n; i++){
			cout<<a[i]<<"     ";
		}
		cout<<endl;
	}
}
void Sinh(int &ok, int n, int a[]){
	int dem1=0;
	for(int i=0; i<n; i++){
		if(a[i]==1){
			dem1++;
		}
	}
	if(dem1==n){
		ok=0;
	}else
	{
	int id=0;
	for(int i=n-1; i>=0; i--){
		if(a[i]==0){
			a[i]=1;
			id=i;
			break;
		}
	}
	for(int i=id+1; i<n; i++){
		a[i]=0;
	}
}}
void Next(int &ok, int n, int a[]){
	Xaudautien(n,a);
	while(ok){
		Xuat(n,a);
		Sinh(ok,n,a);
	}
}
int main(){
	int ok=1;
	int n; cin>>n;
	int a[n];
	Next(ok,n,a);
}

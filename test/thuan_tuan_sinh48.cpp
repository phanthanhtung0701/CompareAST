#include<bits/stdc++.h>
using namespace std;
int a[1001],n,ok;
void kt(){
	for(int i=1;i<=n;i++)	a[i]=0;
}
void next(){
	int i=n;
	while(i>0 && a[i]==1){
		a[i]=0; i--;
	}
	if(i==0){
		ok=0;
	}
	else{
		a[i]=1;
	}
}
bool check(){
	int l=1,r=n;
	while(l<=r){
		if(a[l]!=a[r])
			return false;
			l++, r--;
	}
	return true;
}
main(){
		cin>>n;
		kt();
		ok=1;
		while(ok){
			if(check()){
				for(int i=1;i<=n;i++){
					cout<<a[i]<<" ";
				}
				cout<<endl;
			}
			next();
		}
		cout<<endl;
}

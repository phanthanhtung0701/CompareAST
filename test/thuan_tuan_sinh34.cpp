#include<bits/stdc++.h>

using namespace std;

int n,a[50]={0};

bool check(){
	for(int i=1;i<=n/2;i++){
		if(a[i] != a[n-i+1]) return false;
	}
	return true;
}
void in(){
	for(int i=1;i<=n;i++) cout<<a[i]<<" ";
	cout<<endl;
}

void sinh(){
	in();
	while(1){
		int i=n;
		while(a[i]==1){
			a[i]=1-a[i];
			i--;
		}
		if(i==0) break;
		else a[i]=1-a[i];
		if(check()) in();
	}
}
int main(){
	cin>>n;
	sinh();
}

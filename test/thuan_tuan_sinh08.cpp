#include<bits/stdc++.h>
using namespace std;
int a[100],n;
int check(int *a){
	int k=n;
	for(int i=1;i<=n;i++){
		if(a[i]!=a[k]) return 0;
		k--;
	}
	return 1;
}
void in(){
	if(check(a)){
	for(int i=1;i<=n;i++) cout<<a[i]<<' ';
	cout<<endl;
}}
void sinh(int i){
	for(int j=0;j<2;j++){
		a[i]=j;
		if(i==n)  in();
		else sinh(i+1);
	}
}
main(){
	cin>>n;
	sinh(1);
}

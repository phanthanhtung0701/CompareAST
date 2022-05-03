#include<bits/stdc++.h>
using namespace std;
int n,a[1000];
void kt(){
	int b=1,c=n;
	while(b<c){
		if(a[b]!=a[c]){
			return;
			
		}
		b++;c--;
	}
	for(int i=1;i<=n;i++)
	cout<<a[i]<<"\t";
	cout<<endl;
	
}
void test(int i){
	for(int j=0;j<=1;j++){
		a[i]=j;
		if(i==n) kt();
		else test(i+1);
	}
}
int main(){
	cin>>n;
	test(1);
	return 0;
	
}


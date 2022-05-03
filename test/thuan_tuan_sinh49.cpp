#include<iostream>
#define MAX 100
using namespace std;
bool DX(int A[],int n){
	for(int i=0;i<n/2;i++){
		if(A[i]!=A[n-i-1]) return false;
	}
return true;
}

int main(){
	int n;
	int A[MAX];
	cin>>n;
	for(int i=0;i<n;i++) A[i]=0;
	for(int i=0;i<n;i++){
		cout<<A[i]<<"\t";
	}
		cout<<endl;
for(int i=n-1;i>=0;i--){
	if(A[i]==0){
		A[i]=1;
		for(int j=i+1;j<n;j++) A[j]=0;
		if(DX(A,n)==true) {
		for(int j=0;j<n;j++) cout<<A[j]<<"\t";
		cout<<endl;
		                 }
		                 i=n;
	         }
	
}
	return 0;
}
#include<iostream>
#include<cmath>

using namespace std;

bool ThuanNghich(int A[],int n){
	for(int i=0,j=n-1;j>i;i++,j--){
		if(A[i]!=A[j]) return false;
	}
	return true;
}

void InCauHinh(int A[],int n){
	for(int i=0;i<n;i++)
		cout<<A[i]<<"	";
	cout<<endl;
}

void DatBang0 (int A[],int n,int vt){
	for(int i=vt;i<n;i++){
		A[i]=0;
	}
}

void SinhSoNhiPhan(int A[],int n){
	InCauHinh(A,n);
	int i=n-1;
	while(i>0){
		if(A[i]==1) i--;
		if(A[i]==0){
			A[i]=1;
			DatBang0(A,n,i+1);
			i=n-1;
			if(ThuanNghich(A,n)==true)
			InCauHinh(A,n);
		}
	}
}


int main(){
	int n;
	cin>>n;
	int A[n]={0};
	SinhSoNhiPhan(A,n);
	return 0;
}
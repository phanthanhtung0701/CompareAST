#include <iostream>
using namespace std;
int n, a[100], b[100];
int dem;
void Xuat(){
	for(int i =1;i<=n;i++){
		cout<<a[i]<<"\t";
	}
	cout<<endl;
}
void Kiemtra(){
	dem =0;
	for(int i =1;i<=n;i++){
		b[i] = a[i];
	}
	for(int i=1;i<=n/2;i++){
		int t = b[i];
		b[i] = b[n-i+1];
		b[n-i+1] = t;
	}
	for(int i=1;i<=n;i++){
		if(a[i]==b[i]){
			dem++;
		}
		
	}
}
void Try(int i){
	for (int j =0;j<=1;j++){
		a[i] = j;
		if(i==n){
			Kiemtra();
			if(dem==n){
				Xuat();
			}	
		}
		else Try(i+1);
	}
}


int main(){
	cin>>n;
	Try(1);
	
}
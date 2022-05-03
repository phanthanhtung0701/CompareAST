#include<bits/stdc++.h>
using namespace std;
int main(){
		int n;
		cin >> n ;
		int a[n+1];
		for(int i=1;i<=n;i++){
			a[i]=0;
		}
		while(true){
			int m=0;
			int h=n;
			while(a[h]==1 && h>0) h--;
			if(h==0){
				break;
			}
			for(int i=1;i<=n;i++){
				if(a[i]!=a[n-i+1]){
					m=1;
				}
			}
			if(m==0){
				for(int i=1;i<=n;i++){
					cout << a[i] << " ";
				}
				cout << endl;
			}
		for(int i=h;i<=n;i++){
				a[i]=1-a[i];
		}
	}
		for(int i=1;i<=n;i++){
			cout << "1" << " ";
	}
	return 0;
}
#include<iostream>
using namespace std;
int n, B[20];
int check(){
	int l=1, r=n;
	while(l<r){
		if(B[l]!=B[r]) return 0;
		l++; r--;}
		return 1;
}
void in(){
    for(int i=1;i<=n;i++){
    	if(check())  cout << B[i] << " ";}
    	cout<<endl;
}
void Try(int i){
    for(int j = 0; j <= 1; j++){
        B[i] = j;
        if(i == n ) in();
        else Try(i + 1);
    }
}
int main(){
    cin >> n;
    Try(1);
}

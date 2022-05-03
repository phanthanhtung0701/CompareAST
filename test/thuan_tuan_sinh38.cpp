#include<bits/stdc++.h>
using namespace std;
int n,a[1000],b[1000]={0}, ok =1;
bool check(int a[],int n){
    int i=1;
    while(i<n){
        if(a[i]!=a[n]) return false;
        i++;
        n--;
    }
    return true;
}
void in(){
    if(check(a,n)){
    for(int i=1;i<=n;i++) {
        cout << a[i] <<" ";
    }
    cout << "\n";
    }
}
void next(int i){
    for(int j=0;j<=1;j++){
        a[i]=j;
        if(i==n) in();
        else next(i+1);
    }
}
int main(){
        cin >> n;
        for(int i=1;i<=n;i++) a[i]= 0;
        next(1);
}
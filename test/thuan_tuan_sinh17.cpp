#include<bits/stdc++.h>
using namespace std;
int a[20], n;
void in(){
    for(int i=1; i<=n; i++)
        cout<<a[i]<<" ";
    cout<<endl;
}
void res(){
    int count=0;
    for(int i=1; i<=n/2+1; i++)
        if(a[i]!=a[n-i+1])
            count++;
    if(count==0) in();
}
void np(int i){
    for(int j=0; j<=1; j++){
        a[i]=j;
        if(i==n) res();
        else np(i+1);
    }
}
main(){
    cin>>n;
    np(1);
}
// 1 2 3 4 5 6
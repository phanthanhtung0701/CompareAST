#include<bits/stdc++.h>
using namespace std;
int main (){
    
        int n;
        cin>>n;
        int a[n];
        memset(a,0,sizeof(a));
        int check=0,ok,check1=0;
        for(int i=0;i<n;i++) cout<<a[i]<<" ";
        cout<<endl;
        if(n%2==0) {check=n/2;ok=1;}
        else{ check=(n+1)/2;ok=2;}
        for(int i=n-1;i>=0;i--){
            if(a[i]==0){
                a[i]=1;
                for(int j=i+1;j<n;j++) a[j]=0;
                if (ok==1) {//chan
                int l=0,r=n-1;
                    while(l<=check){
                        if(a[l]!=a[r]){
                            check1=-1;
                            break;
                        }
                        l++;r--;
                    }
                    if(check1!=-1){ 
                        for(int k=0;k<n;k++) cout<<a[k]<<" ";
                    cout<<endl;}
                    check1=0;
                }
                else if(ok==2){
                    //le;
                    int l=0,r=n-1;
                    while(l<check){
                        if(a[l]!=a[r]){
                            check1=-1;
                            break;
                        }
                        l++;r--;
                    }
                    if(check1!=-1){ 
                        for(int k=0;k<n;k++) cout<<a[k]<<" ";
                    cout<<endl;}
                    check1=0;
                }
            i=n;
            }
        }

}
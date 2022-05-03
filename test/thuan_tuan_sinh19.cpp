#include <bits/stdc++.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
using namespace std;

int a[100],ok=1,n;

void init()
{
	for(int i=1;i<=n;i++){
		a[i]=0;
	}
}

void in()
{
	for(int i=1;i<=n;i++){
		cout<<a[i]<<"\t";
	}
	cout<<endl;
}

bool check()
{
	int l=1;
	int r=n;
	while(l<r){
		if(a[l]!=a[r]){
			return false;
		}
		l++;
		r--;	
	}
	return true;
}

void sinh()
{
	int i=n;
	while(i>=1 && a[i]==1 ){
		i--;
	}
	if( i==0 ){
		ok=0;
	}
	else{
		a[i]=1;
		for(int j=i+1;j<=n;j++){
			a[j]=0;
		}
	}
}

main()
{
//	int test;
//	cin>>test;
//	for(int t=0;t<test;t++)
//	{
		init();
		cin>>n;
		while( ok==1 ){
			if( check() ){
				in();
			}
			sinh();
		}
//	}
}
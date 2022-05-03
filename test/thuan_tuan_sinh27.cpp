#include<iostream>
using namespace std;

void init(int *&b,int n)
{
	b=new int[n+1];
	for(int i=1;i<=n;i++) b[i]=0;
}
bool ktratn(int *b,int n)
{
	int set=1;
	for(int i=1;i<=n/2;i++)
		{
			if(b[i]!=b[n-i+1]) set=0;
		}
		return set;
}
void daybit(int *b,int n,int &OK)
{
	int i=n;
	while(i>0 && b[i]==1)
	{
		b[i]=0;
		i--;
	}
	b[i]=1;
	if(i<=0) OK=0;
}
void xuattn(int n){
	int *b;
	int OK=1;
	init(b,n);
	while(OK==1){
		if(ktratn(b,n)==1){
			for(int i=1;i<=n;i++)
			cout<<"\t"<<b[i];
			cout<<"\n";
		}
		
		daybit(b,n,OK);
	}
	delete[]b;
}
int main(){
	int n;
	cin>>n;
	xuattn(n);
	return 0;
}
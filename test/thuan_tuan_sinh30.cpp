#include<bits/stdc++.h>
using namespace std;
void nhap(int a[], int n)
{
	for (int i=0;i<n;i++)
		a[i]=0;
}
bool check(int a[],int n)
{
	int l=0;
	int r=n-1;
	while(l<r)
	{
		if (a[l]!=a[r])
			return false;
		else{
			l++;
			r--;
		}
	}
	return true;
}
void xuat(int a[],int n)
{
	for (int i=0;i<n;i++)
		cout<<a[i]<<" ";
		cout<<endl;
}
void nextbinary(int a[],int n)
{
	xuat(a,n);
	while(1)
	{
		int i=n-1;
		while(i>=0&&a[i]==1)
			i--;
		if (i<0)	break;
		else
		{
			a[i]=1;
			for (int j=i+1;j<n;j++)
				a[j]=0;
			if (check(a,n))
				xuat(a,n);
		}
	}
}
int main()
{

		int n;
		cin>>n;
		int a[n];
		nhap(a,n);
		nextbinary(a,n);

}
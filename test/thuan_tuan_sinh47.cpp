#include <bits/stdc++.h>
using namespace std;

int n;	
int x[105] ;
void ktao()
{
	for(int i = 0; i < n; i++) x[i] = 0;
}
bool Check()
{
	for(int i = 0; i < n; i++)
	{
		if(x[i]==0) return 0;
	}
	return 1;
}
void In()
{
	for(int i = 0; i < n; i++) cout << x[i] << " ";
	cout << endl;
}
void Sinh()
{
	int i = n-1;
	while(x[i]==1) i--;
	for(int j = i; j <= n; j++) x[j] = 1 - x[j]; 
	
}
bool Tn()
{
	for(int i = 0; i < n/2; i++) 
	{
		if(x[i]!=x[n-i-1]) return 0;
	}
	return 1;
}
int main()
{
	cin >> n;
	ktao();
	In();
	while(!Check())
	{
		Sinh();
		if(Tn()) In();
	}
}

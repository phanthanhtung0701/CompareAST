#include<bits/stdc++.h>
using namespace std ;
void in( int a[] , int n ) {
	for ( int i = 0 ; i < n ; i++ ) cout << a[i] << " " ;
	cout << endl ;
}
int ktr ( int a[] , int n ) {
	for ( int i = 0 ; i < n ; i++ ) if ( a[i] != a[n-1-i] ) return 0 ;
	return 1 ;
}
void sinhnhiphan ( int n ) {
	int a[n] ;
	for ( int i = 0 ; i < n ; i++ ) a[i] = 0 ;
	while ( 1 ) {
		if ( ktr(a,n) == 1 ) in(a,n) ;
		int i = n - 1 ;
		while ( i >= 0 && a[i] == 1 ) {
			a[i] = 0 ;
			i-- ;
		}
		if ( i >= 0 ) a[i] = 1 ;
		else break ;
	}
}
int main () {
	int n ;
	cin >> n ;
	sinhnhiphan(n) ;
}

/*
n = 4
	0 0 0 0
	0 1 1 0
	1 0 0 1
	1 1 1 1
*/


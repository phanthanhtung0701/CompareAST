#include <iostream>
using namespace std;
int* b, n, i, ok = 1;
void init()
{
	b = new int[n + 1];
	for (int i = 1; i <= n; i++) b[i] = 0;
}
bool kt()
{
	int set = 1;
	for (int  i = 1; i <= n / 2; i++) {
		if (b[i] != b[n - i + 1]) set = 0;
	}
	return set;
}
void nextbit()
{
	i = n;
	while (i > 0 && b[i] == 1) {
		b[i] = 0;
		i--;
	}
	b[i] = 1;
	if (i <= 0) ok = 0;
}
void in(int n)
{
	init();
	while (ok == 1) {
		if (kt() == 1) {
			for ( i = 1; i <= n; i++)
				cout << "\t" << b[i];
			cout << "\n";
		}
		nextbit();
	}
	delete[]b;
}
/*void show(int *b,int n)
{
	int* b; int ok = 1;
	init(b,n);
	while (ok == 1) {
		if (kt() == 1) {
			for (int i = 1; i <= n; i++)
				cout << "\t" << b[i];
			cout << "\n";
		}
		nextbit();
	}
	delete[]b;
}*/
int main()
{
	cin >> n;
	in(n);
	return 0;
}
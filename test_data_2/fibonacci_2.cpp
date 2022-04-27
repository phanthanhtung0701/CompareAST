#include <stdio.h>
#include <conio.h>
int Fbnc(int a){
    if (a == 1 || a == 2) return 1;
    //return Fbnc(a - 1) + Fbnc(a - 2);
    int b = Fbnc(a - 2);
    return b;
}

//int main(){
//	int n;
//	printf("nhap n: ");
//	scanf("%d", &n);
//	printf("So Fibonacci thu %d la: %d", n, Fibonacci(n));
//	return 0;
//}

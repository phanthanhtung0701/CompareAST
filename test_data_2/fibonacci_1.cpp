#include <stdio.h>
#include <conio.h>

// Ngay 20/04/2022 - NamNT
// Ham Fibonacci dau vao la 1 so nguyen duong n
int Fibonacci(int n){
    if (n==1||n==2){
        return 1;
    }

    // Return noi dung can tim F(n) = F(n-1) + F(n-2)
    return Fibonacci(n - 1)+Fibonacci(n - 2);
}

//int main(){
//	int n;
//	printf("nhap n: ");
//	scanf("%d", &n);
//	printf("So Fibonacci thu %d la: %d", n, Fibonacci(n));
//	return 0;
//}

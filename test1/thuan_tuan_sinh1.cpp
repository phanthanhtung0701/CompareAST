#include<stdio.h>

int nextBitString(int a[], int n){
    int k;
    for (k = n; k >= 1; k--){
        if (a[k] == 0) break;
    }
    for (int i = k; i <= n; i++){
        a[i] = 1 - a[i];
    }
    for (k = n; k >= 1; k--){
        if (a[k] == 0) break;
    }
    if (k == 0) return 1;
    else return 0;
}

void printfBitString(int a[], int n){
    for (int i = 1; i <= n; i++) printf("%d ", a[i]);
    printf("\n");
}

int thng(int a[], int n){
	for (int i = 1; i <= n/2 + 1; i++){
		if(a[i] != a[n - i + 1]) return 0;
	}
	return 1;
}

int main(){
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 1; i <= n; i++) a[i] = 0;
    int last = 0;
    while (!last){
    	if(thng(a, n)){
	        printfBitString(a, n);
		}
		last = nextBitString(a, n);
    }
    printfBitString(a, n);
    return 0;
}

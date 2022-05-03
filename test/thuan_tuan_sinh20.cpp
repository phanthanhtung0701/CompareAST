#include<stdio.h>
#include<math.h>
void bin( int B[], int n ){
    int i = n;
    while (i >0 && B[i] == 1) {
        B[i] = 0;
        i--;
    }
    if(i == 0) return;
    else B[i] = 1;
}
void xuat(int B[],int n){
	for(int i=1;i<=n;i++)printf("%d ",B[i]);
	printf("\n");
}
void ktra(int B[],int n){
	int i=1,j=n,test=1;
	while(i<j&&test){
		if(B[i]==B[j]){
			i++;j--;test=1;
		}else {test=0;}
	}
	if(test==1){xuat(B,n);
	}
}
int main(){
	int B[1000]={},n,dem;
	scanf("%d",&n);
	for(int i=1; i<=n;i++)printf("%d ",B[i]=0);
	printf("\n");
	for(int i=1;i<pow(2,n);i++){
		bin(B,n);
		//xuat(B,n);
		ktra(B,n);
	}
}

#include<stdio.h>
int n,a[100];
bool ok=0;
void khoitao(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		a[i]=0;
	}
}
void in(){
	for(int i=1;i<=n;i++){
		printf("%d\t",a[i]);
	}
	printf("\n");
}
int tn(){
	int x=1,y=n;
	while(x<y){
		if(a[x]!=a[y]){
			return 0;
		}
		else {
			x++;
			y--;
		}
	}
	return 1;
}
void sinhtiep(){
	int i=n;
	while(i>0&&a[i]==1){
		i--;
	}
	if(i==0)ok=1;
	else {
		a[i]=1;
		for(int j=i+1;j<=n;j++){
			a[j]=0;
		}

	}
}
 int main(){
 	khoitao();
 	while(!ok){
 		if(tn()){
 		in();
 	}
 		sinhtiep();
	 }
 	return 0;
 }
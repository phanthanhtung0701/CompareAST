#include<stdio.h>
#include<string.h>
int t,k,i,j,ok;
int arr[1005];
void in(){
	for(i=1;i<=k;i++)
	printf("%d ",arr[i]);
	printf("\n");
}
int thuannghich(){
	int d=1,c=k;
	while(d<c){
		if(arr[d]!=arr[c])
		return 0;
		d++;	c--;
	}
	return 1;
}
void sinh(){
	int i=k;
	while(i>0 && arr[i]==1)	i--;
		if(i<=0){
			ok=1;
		}
		else{
			arr[i]=1;
			for(j=i+1;j<=k;j++){
				arr[j]=0;
			}
		}
}
int main(){
	scanf("%d",&k);
		ok=0;
		for(i=1;i<=k;i++)
		arr[i]=0;
		while(!ok){
		if(thuannghich()==1)
		in();
		sinh();	
		}
}

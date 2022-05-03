#include <stdio.h>
int a[20];
int n, len;
void find(int k)
{
    int i, j;
    if (k > (n+1)/2)
    {
      for (j=1;j<=(n+1)/2; j++) printf("%d ",a[j]);
      for (j=len;j>=1; j--) printf("%d ",a[j]);
      printf("\n");
      return;
    }
    for (i=0;i<=1; i++)
    {
        a[k]=i;
        find(k+1);
    }
}
int main()
{
  //printf("\nNhap n=");
  scanf("%d", &n);
  len=(n%2) ? ((n-1)/2) : (n/2);
  find(1);
}

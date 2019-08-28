#include<stdio.h>
int comb(int s,int e,int l,int*a,int p,int n,int b,int x)
 {
   int i,m;
   for(i=s;i<e;i++)
     {
       p=p*(*(a+i));
           m=p;
            if(l!=1)
            {
            comb(s-1,e-1,l-1,*a,p,n,b,x);
            }
            else
              {
                if(e==(x-l-1))
                {
                 
                return b;
                }
              }
            if(p==n)
             {
               b=b+1;
             }
             p=m;
        }
        return b;
 }
void main()
{
int i,j=0,n,l,a[30],c;
 printf("enter the number and number of distinct numbers:");
 scanf("%d%d",&n,&l);
 for(i=1;i<=(n/2);i++)
{
 if(n%i==0)
{
a[j]=i;
j=j+1;
}
}
a[j]=n;
c=comb(l-n,j+1,l,a,1,n,0,j+1);
printf("%d\n",c);
}

import java.util.*;
import java.lang.*;
import java.io.*;


class ADAMAT
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
            int n=sc.nextInt();
            int a[][]=new int[n][n];
            int i,j;
            for(i=0;i<n;i++)
            {
                for(j=0;j<n;j++)
                {
                    a[i][j]=sc.nextInt();
                }
            }
            int count=0;
            j=n;
            int f=0;
            for(i=n-1;i>0;i--)
            {
                if( ( (a[0][i]!=j)&&(f==0) ) || ( (a[0][i]==j)&&(f==1) ) )
                {
                    count++;
                    f=(f+1)%2;
                }
                j--;
            }
            System.out.println(count);

        }
	}
}

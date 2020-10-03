import java.util.*;
import java.lang.*;
import java.io.*;

class TREE2
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0)
		{
		    HashMap<Long,Integer> map=new HashMap<>();
		    int n=sc.nextInt();
		    int count=0;
		    long a[]=new long[n];
		    int i;
		    for(i=0;i<n;i++)
		    {
		        a[i]=sc.nextLong();
		        if(a[i]==0)
		        {
		            continue;
		        }
		        else
		        {
		            if(map.containsKey(a[i])==true)
		            continue;
		            else
		            {
		            count++;
		            map.put(a[i],1);
		            }
		        }
		    }
		    System.out.println(count);
		}
	}
}

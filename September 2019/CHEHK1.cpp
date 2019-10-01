//Ajinkya Taranekar
#include <iostream>
#include <math.h>
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define TEST(tc) llr (tc); cin>>tc; while(tc--) 
#define llr long long register int 
using namespace std;

int main() {
	// your code goes here
	fio
	TEST(tc){
	    llr n,m;
	    cin>>n>>m;
	    llr diag_edge=(n*(n+1))/2;//diag_edge=diagonals+edges=n(n-1)/2 + n
	    
	    if((m>diag_edge)||(m<n-1))//minimum requriment else network can't be formed
	        cout<<"-1\n";
	    else if(n==1&&m==0)
	        cout<<"0\n";
	    else if((n==2&&m==1)||(n==1&&m==1))
	        cout<<"1\n";
	    else if(m<=n+1)
	        cout<<"2\n";
	    else if(m>n+1&&m<=2*n)
	        cout<<"3\n";
	    else //figured out this part after 4hrs...
	        cout<<ceil((2*(double)(m)/(double)n))-1<<"\n";
	}
	return 0;
}

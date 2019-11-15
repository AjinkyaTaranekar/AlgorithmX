#include<iostream>
#include<math.h>
#define TESTS(tc) ll (tc); cin>>(tc); while((tc)--)
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 
#define ll long long int
#define f(i,a,b) for(register ll i=a; i<b; i++)
using namespace std;
int binaryToDecimal(int n) 
{ 
    int num = n; 
    int dec_value = 0; 
  
    int base = 1; 
  
    int temp = num; 
    while (temp) { 
        int last_digit = temp % 10; 
        temp = temp / 10; 
  
        dec_value += last_digit * base; 
  
        base = base * 2; 
    } 
  
    return dec_value; 
} 
int main(){
    fio;
    TESTS(tc){
        int participants;
        cin>>participants;
        ll wepons,result=0;
        f(i,0,participants){
            cin>>wepons;
            result^=binaryToDecimal(wepons);
        }
        cout<<__builtin_popcount (result)<<"\n";
    }
	return 0;
}

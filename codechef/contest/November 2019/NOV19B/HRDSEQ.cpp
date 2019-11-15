#include<iostream>
#define TESTS(tc) ll (tc); cin>>(tc); while((tc)--)
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 
#define ll long long int
#define f(i,a,b) for(register ll i=a; i<b; i++)
using namespace std;

int hardSequence[128];

void fillHardSequence(){
    hardSequence[0] = 0;
    f(i,1,128){
        bool flag = true;
        for(int j =i-2; j >= 0; j--){
            if(hardSequence[i-1] == hardSequence[j]){
                hardSequence[i] = i - j - 1;
                flag = false;
                break;
            }
        }
        if(flag) 
            hardSequence[i] = 0;
    }
}

int main(){
    fillHardSequence();
    fio;
    TESTS(tc){
        int num,res=1;
        cin>>num;
        f(i,0,num-1){
            if(hardSequence[num-1]==hardSequence[i])
                res++;
        }
        cout<<res<<"\n";
        
    }
	return 0;
}

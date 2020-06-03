#include<iostream>
#include<string>
#define TESTS(tc) ll (tc); cin>>(tc); while((tc)--)
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 
#define ll long long int
#define f(i,a,b) for(register ll i=a; i<b; i++)
using namespace std;

int main(){
    fio;
    int n, t;
    cin >> n >> t;
    
    string s;
    cin >> s;
    
    while (t--){
        f(i,0,n){
            if (s[i+1] == 'G' && s[i] == 'B'){
                s[i+1] = 'B';
                s[i] = 'G';
                i++;
            }
        }
    }
    cout << s << "\n";
    return 0;
}
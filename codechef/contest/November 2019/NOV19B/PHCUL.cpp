#include<iostream>
#include<math.h>
#include<limits.h>
#include<iomanip>
#define TESTS(tc) ll (tc); cin>>(tc); while((tc)--)
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 
#define ll long long int
#define f(i,a,b) for(register ll i=a; i<b; i++)
#define max (double)ULONG_MAX
using namespace std;

double distance( register ll initalPoint_x,int initalPoint_y, int finalPoint_x,int finalPoint_y){
    return sqrt(pow(initalPoint_x-finalPoint_x,2) + pow(initalPoint_y-finalPoint_y,2));
}

int main(){
    fio;
    TESTS(tc){
        ll O_x, O_y;
        cin >> O_x >> O_y;
    
        ll N,M,K;
        cin >> N >> M >> K;
        
        ll X[2*N], Y[2*M], Z[2*K];
        
        f(i,0,2*N)
            cin >> X[i];
        
        f(i,0,2*M)
            cin >> Y[i];
        
        f(i,0,2*K)
            cin >> Z[i];
        
        double OX[N],OY[M];
        
        for( register ll i= 0 ; i<2*N; i+=2)
            OX[i/2] = distance(O_x,O_y,X[i],X[i+1]);
    
        for( register ll i= 0 ; i<2*M; i+=2)
            OY[i/2] = distance(O_x,O_y, Y[i], Y[i+1]);
    
        double XY[M],YX[N];
        
        for( register ll i= 0 ; i<2*M; i+=2){
            XY[i/2] = max;
            for( register ll j= 0 ; j<2*N; j+=2)
                XY[i/2] = min(XY[i/2],distance(Y[i], Y[i+1],X[j],X[j+1])+OX[j/2]);
        }
        
        for( register ll i= 0 ; i<2*N; i+=2){
            YX[i/2] = max;
            for( register ll j= 0 ; j<2*M; j+=2)
                YX[i/2] = min(YX[i/2],distance(X[i], X[i+1],Y[j],Y[j+1])+OY[j/2]);
        }
        
        double minimumDist = max;
    
        for( register ll i= 0 ; i<2*K; i+=2){
            for( register ll j= 0 ; j<2*N; j+=2)
                minimumDist = min(minimumDist, distance(Z[i],Z[i+1],X[j],X[j+1])+YX[j/2]);
                
            for( register ll j= 0 ; j<2*M; j+=2)
                minimumDist = min(minimumDist, distance(Z[i],Z[i+1],Y[j],Y[j+1])+XY[j/2]);
        }
        
        cout << std::setprecision(11) << minimumDist << "\n";
   }
	return 0;
}

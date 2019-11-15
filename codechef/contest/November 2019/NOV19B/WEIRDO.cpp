//something went wrong :(

#include<iostream>
#include<math.h>
#include<vector>
#include<iomanip>
#define TESTS(tc) ll (tc); cin>>(tc); while((tc)--)
#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 
#define ll long long int
#define f(i,a,b) for(register ll i=a; i<b; i++)
using namespace std;
bool isVowel(char ch) 
{ 
    ch = toupper(ch); 
    return (ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U'); 
} 
  
int countVowels(string recipe) 
{ 
    int count = 0; 
    for (int i=0; i<recipe.length(); i++) 
        if (isVowel(recipe[i]))  
            ++count; 
    return count; 
} 

bool distinguishInSubstring(string recipe){
     for (int i = 0; i < recipe.length()-1; i++)  
        if(!isVowel(recipe[i]) && !isVowel(recipe[i+1]) )
            return false;
     return true;
}

vector<string> alice,bob;

void identifyingTheRecipes(string recipe){
        if(2*countVowels(recipe)>=recipe.length() && distinguishInSubstring(recipe))
            alice.push_back(recipe);
        else
            bob.push_back(recipe);
}
vector<int> smallestInCol(int mat[][26],int n,int m)
{   
    vector<int> count(26,1);
    if(n==1)
        return count;
    int minm;
    f(i,0,m){ 
        minm = mat[0][i];
        f(j,1,n) 
            if (mat[j][i] < minm)
                minm= mat[j][i];
        if(minm!=0)
            count[i]+=1;   
    }
    return count;
}    
double findTheSc(vector<string> recipes)
{   
    int freq[recipes.size()][26];
    f(i,0,recipes.size())
        f(j,0,26)
            freq[i][j]=0;
    
    int total[26] ={0};
    
    f(i,0,recipes.size())
        f(j,0,((recipes[i]).size()))
        {
            char c = recipes[i][j];    
            freq[i][c - 'a'] += 1; 
        }
    string ovarallrecipe= "";
    
    f(i,0,recipes.size())
        ovarallrecipe+=recipes[i];
    
    f(i,0,ovarallrecipe.length())
        total[(ovarallrecipe[i]) - ('a')] += 1; 
    
    vector<int> count;
    count.clear();
    count= smallestInCol(freq,(recipes).size(),26); 
    
    double sc=1.0;
    f(i,0,26)
        if (total[i]!=0)
            sc*=count[i]/pow(total[i],(recipes).size());
    
    return sc ;
}    
double ratio(){
    return findTheSc(alice)/findTheSc(bob);
}

int main()
{   
    fio;
    TESTS(tc){
        int recipes;
        cin>>recipes;
        string recipe[recipes];
        f(i,0,recipes){
            cin>>recipe[i];
            identifyingTheRecipes(recipe[i]);
        }
        if(ratio()>10000000)
            cout<<"Infinity"<<"\n";
        else
            cout<<setprecision(7)<<ratio()<<"\n";
            
       /* f(i,0,alice.size())
            cout<<alice[i]<<" ";
        cout<<"\n";
        f(i,0,bob.size())
           cout<<bob[i]<<" ";
        cout<<"\n";    
        */
        alice.clear();
        bob.clear();
    }         
    
}
    

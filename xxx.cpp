#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long int t;
    cin >> t;

    while(t--){
        long long int n,e,h;
        long int A,B,C;

        cin >> n >> e >>h>>A>>B>>C;
        long long int ans;
        ans=res(n,e,h,A,B,C)
        if(ans==1e15){
            cout << -1 <<endl;
        }
        else
        {
            cout << ans << endl;
        }


    }
    return 0;
}

long  long int res(long long n,long long e,long long h, long long A, long long B, long long C){
    if(n<= 0){
        return 0;
    }
    long long ans = 1e13;
    
    if((n<=e) && (n<=h)){

        ans= minv(ans,n*C);

        


    }

}
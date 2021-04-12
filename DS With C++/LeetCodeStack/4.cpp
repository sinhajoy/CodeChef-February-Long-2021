#include<bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> a={1,2};
    vector<int> b={3,4};
    vector<int> x;

    merge(a.begin(),a.end(),b.begin(),b.end(),x.begin());
    sort(x.begin(),x.end());

    return 0;

}
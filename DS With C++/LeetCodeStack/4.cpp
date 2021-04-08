#include<bits/stdc++.h>

using namespace std;
double CalcMHWScore(vector<int> scores)
{
  size_t size = scores.size();

  if (size == 0)
  {
    return 0;  // Undefined, really.
  }
  else
  {
    sort(scores.begin(), scores.end());
    if (size % 2 == 0)
    {
      return (scores[size / 2 - 1] + scores[size / 2]) / 2;
    }
    else 
    {
      return scores[size / 2];
    }
  }
}
int main()
{
    vector<int> a={1,2};
    vector<int> b={3,4};
    vector<int> x(a.size()+b.size());

    merge(a.begin(),a.end(),b.begin(),b.end(),x.begin());
    sort(x.begin(),x.end());

    cout<< CalcMHWScore(x);

    return 0;

}
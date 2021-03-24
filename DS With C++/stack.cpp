#include<bits/stdc++.h>
using namespace std;

void showstack(stack <int> s){
    while (!s.empty())
    {
        cout << '\t' << s.top();
        s.pop();
        
    }

    cout << '\n';
}


int main()
{
    stack <int> s;
    s.push(10);
    s.push(30);
    s.push(20);
    s.push(5);
    s.push(1);

    cout << "Stack is: ";
    showstack(s);

    cout << "\ns.size() :" << s.size();
    cout << "\ntop:" << s.top();

    cout << "\n Pop :";
    s.pop();
    showstack(s);

    return 0;

}
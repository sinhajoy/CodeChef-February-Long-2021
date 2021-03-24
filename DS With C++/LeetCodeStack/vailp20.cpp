#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack <char> k;
        for(int i=0;i<s.length();i++){
            if(s[i] == '(' || s[i] == '{' || s[i] == '['){
                k.push(s[i]);
            }
            else if(s[i] == ')' || s[i] == '}' || s[i] == ']'){
                if (k.empty()){
                    return false;
                }
                else if(s[i]==')' && k.top() != '('){
                    return false;
                }
                else if(s[i]=='}' && k.top() != '{'){
                    return false;
                }
                else if(s[i]==']' && k.top() != '['){
                    return false;
                }
                else
                    k.pop();
            }
            
        }
        if(k.empty())
            return true;
        else
            return false;
    }
};

//Input: s = "()[]{}"
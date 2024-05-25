#include <iostream>
#include <stack>
using namespace std;

class isValidParen {
public:
    bool isValid(string s) {
       stack<char> st;
       bool val=false;
       for(int i=0;i<s.length();i++){
        if(s.at(i)=='('||s.at(i)=='['||s.at(i)=='{'){
st.push(s.at(i));
val=false;
        }
        else if(st.size()>=1){
         if(s.at(i)==')'&&st.top()=='('){
st.pop();
if(i==s.length()-1)
val=true;
        }
        
        else if(s.at(i)==']'&&st.top()=='['){
st.pop();
if(i==s.length()-1)
val=true;
        }
        
        else if(s.at(i)=='}'&&st.top()=='{'){
st.pop();
if(i==s.length()-1)
val=true;
        }
        
        else{
         val= false;
         break;}
       }
       else{
        val = false;
       break;
       }
       
    }
    return val;
    }
};

int main()
{
    string s="(){}}{";
    isValidParen ch;
    cout << ch.isValid(s); 
    
}
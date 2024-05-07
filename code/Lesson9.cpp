#include<iostream>
#include<string>
#include<stack>
#include<queue>
using namespace std;

int main(){
    string input;
    cin>>input;
    stack<char> left;
    bool flag=true;
    for(int i=0;i<input.length();++i){
        if(input[i]=='('||input[i]=='['||input[i]=='{'){
            left.push(input[i]);
        }else{
            switch(input[i]){
                case ')':
                    if(left.top()!='(') flag=false;
                    break;
                case '}':
                    if(left.top()!='{') flag=false;
                    break;
                case ']':
                    if(left.top()!='[') flag=false;
                    break;
                default:
                    break;
            }
            if(!flag) break;
        }
    }
    cout<<((flag)?"Yes":"No")<<endl;
}
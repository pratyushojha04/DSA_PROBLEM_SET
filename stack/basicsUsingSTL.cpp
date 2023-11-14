#include <iostream>
#include<stack>
using namespace std;
int main() {
    stack<int>s;
    s.push(2);
    s.push(3);
    cout<<"the top element in the stack is "<<s.top();
  
  return 0;
}
#include <iostream>
#include<stack>
using namespace std;
//stck can be impleented in two forms 
//linkedlist and array

class Stack{
    //properties
    public :
    int *arr;
    int top;
    int size;
    //behaviour
    Stack(int size){
        this->size=size;
        arr=new int[size];
        top=-1;

    }
    void push(int element){}
    void pop(int element){}

    void top(int element){}

    int peak(int element){}
    bool isEmpty(){}








}



int main() {
    
  return 0;
}
#include <iostream>
using namespace std;
int main()
{
    int n = 3;

    int arr[3] = {1, 4, 2};
    int key = 4;
    
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            cout << "the element is at " << i;
        }
        else
        {
            cout << "the element did not found";
        }
    }

    return 0;
}
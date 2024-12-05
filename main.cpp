//C++ code to find wheather a given number is odd or even
#include<iostream>

using namespace std;

bool OE(int n)
{   
   return n % 2 == 0; 
}

int main()
{   int n;
    cout<<"Enter a value: ";
    cin>>n;
    (OE(n)) ? cout<<"Even\n" : cout<<"Odd\n";
     
    return 0;   
}
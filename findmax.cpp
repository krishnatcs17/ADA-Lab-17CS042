#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter N: ";
    cin>>n;
    int arr[n];
    cout<<"Enter the numbers:\n";
    for(int i=0; i<n; i++) {
        cin>>arr[i];
    }
    int maxi = arr[0];
    for(int j=1; j<n; j++){
        if(arr[j] > maxi)
            maxi = arr[j];
    }
    cout<<"Maximum = "<<maxi<<endl;
    return 0;
}

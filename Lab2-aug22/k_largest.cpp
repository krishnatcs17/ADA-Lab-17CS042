#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

void k_largest(int arr[],int n,int k)
{
    int maxi;
    for(int i=0; i<k; i++) {
        maxi = i;
        for(int j=i+1; j<n; j++) {
            if(arr[j] > arr[maxi])
                maxi = j;
        }
        int temp = arr[i];
        arr[i] = arr[maxi];
        arr[maxi] = temp;

        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    int n,k;
    cout<<"Enter n: ";
    cin>>n;
    int arr[n];
    cout<<"Elements: ";
    for(int i=0; i<n; i++)
        cin>>arr[i];
    cout<<"Enter k: ";
    cin>>k;
    cout<<k<<" largest elements are: ";
    k_largest(arr, n, k);
    return 0;
}

/*
---OUTPUT---

Enter n: 6
Elements: 3 8 12 4 6 1
Enter k: 3
3 largest elements are: 12 8 6 

*/
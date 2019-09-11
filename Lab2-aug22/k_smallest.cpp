#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

void k_smallest(int arr[],int n,int k)
{
    int mini;
    for(int i=0; i<k; i++) {
        mini = i;
        for(int j=i+1; j<n; j++) {
            if(arr[j] < arr[mini])
                mini = j;
        }
        int temp = arr[i];
        arr[i] = arr[mini];
        arr[mini] = temp;
    }
    cout<<k<<" smallest = "<<arr[k-1]<<endl;
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
    k_smallest(arr, n, k);
    return 0;
}

/*
--OUTPUT--

Enter n: 6
Elements: 18 4 12 6 10 8
Enter k: 4
4 smallest = 10

*/
#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
using namespace std;

int main()
{
    int text;
    int arr[30], flag =0, t=0, tc, temp;
    fstream infile;
    infile.open ("testcases.txt", ios::in );

    string str;
    infile >> tc;
    for(int i=0; i<tc; i++) {
        int s, k;
        infile >> s;
        infile >> k;
        for(int j=0; j< s; j++){
            infile >> temp;
            arr[j] = temp;
        }
        int l=0, h=s-1, m;
        while(h >= l) {
            m = (l+h)/2;
            if(arr[m] == k){
                cout<<1<<endl;
                flag=1;
                break;
            }
            else if(k > arr[m])
                l = m+1;
            else
                h = m-1;
        }
        if(flag  == 0)
            cout<<-1<<endl;
        flag=0;
    }
    infile.close();
    return 0;
}

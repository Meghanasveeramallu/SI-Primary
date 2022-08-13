#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
bool valid(long long int a[],long long int b[],long long int pwr[],int i,int j,int n){
    long long int k=1e9 + 7;
    long long fh=(a[j]-(i==0 ? 0 : a[i-1])+k)%k;
    long long bh=(b[i]-(j==n-1 ? 0 : b[j+1])+k)%k;
    int sppfh=i+1;
    int sppbh=n-j;
    int d=abs(sppfh-sppbh);
    if (sppfh<sppbh)
        fh=(fh*pwr[d])%k;
    else
        bh=(bh*pwr[d])%k;
    
    return fh==bh;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        long long int k=1e9 + 7;
        int p=31;
        long long int pwr[n+1];
        long long int a[n];
        long long int b[n];
        pwr[0]=1;
        a[0]=s[0]*p;
        b[n-1]=s[n-1]*p;

        for(int i=1;i<=n;i++){
            pwr[i]=(pwr[i-1]*p)%k;
        }

        for(int i=1;i<n;i++){
            a[i]=(a[i-1]+s[i]*pwr[i+1])%k;
            b[n-i-1]=(b[n-i]+s[n-i-1]*pwr[i+1])%k;
        }

        int ans=1;
        int loe=0;
        for(int i=1;i<n-1;i++){
            for(int j=loe+1;j<=min(i,n-i-1);j++)
                if (valid(a,b,pwr,i-j,i+j,n))
                    loe=j;
                else
                    break;
        }

        ans=2*loe + 1;

        loe=0;
        for(int i=0;i<n-1;i++){
            if (s[i]==s[i+1]){
                for(int j=loe+1;j<=min(i,n-i-2);j++){
                    if (valid(a,b,pwr,i-j,i+1+j,n))
                        loe=j;
                    else
                        break;
                }
                ans=max(ans,2*loe + 2);
            }
        }

        cout<<ans<<endl;
    }
    return 0;
}

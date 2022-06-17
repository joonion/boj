#include<bits/stdc++.h>
using namespace std;int main(){int n,i,A[10000];cin>>n;for(i=0;i<n;i++)cin>>A[i];if(next_permutation(A,A+n))for(i=0;i<n;i++)cout<<A[i]<<" ";else cout<<-1;}
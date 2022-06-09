#include <bits/stdc++.h>
using namespace std;string D="URDL";int a[]={-1,0,1,0},b[]={0,1,0,-1};int n, m, k;vector<string> A;vector<bool> M;
bool f(int t,int v,int &u,int &l,int &r){int i=v/m,j=v%m; int x=D.find(A[i][j]);if(1<=t&&t<=3){x=(x>=t)?x-t:x-t+4;l+=t;}if(4<=t&&t<=6){x=(x+t-3)%4;r+=t-3;}int c=i+a[x],d=j+b[x];u=c*m+d;return(0<=c&&c<n&&0<=d&&d<m&&!M[u]&&l<=k&&r<=k);}
bool s(int v,int l,int r){if(v==n*m-1)return true;else{for(int t=0;t<7;t++){int u,L=l,R=r;if(f(t,v,u,L,R)){M[u]=true;if(s(u,L,R))return true;M[u]=false;}}return false;}}
int main(){cin>>n>>m>>k;A.resize(n);for(int i=0;i<n;i++)cin>>A[i];M.resize(n*m,false);M[0]=true;cout<<(s(0,0,0)?"Yes":"No");}
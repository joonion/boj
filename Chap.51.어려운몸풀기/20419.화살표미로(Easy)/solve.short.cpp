#include <bits/stdc++.h>
using namespace std;
map<char,int>H={{'U',0},{'R',1},{'D',2},{'L',3}};
int D[][4]={{-1,0,1,0},{0,1,0,-1}};
int n,m,k;
string A[50];
bool mark[50][50];
bool dfs(int i,int j,int l,int r) {
int t,x,L,R,ni,nj;
if(i*m+j==n*m-1)return 1;
for(t=0;t<3;t++) {
L=l;R=r;x=H[A[i][j]];
if(t==1){x=(x+3)%4;L++;}
if(t==2){x=(x+1)%4;R++;}
ni=i+D[0][x];nj=j+D[1][x];
if (L<=k&&R<=k&&0<=ni&&0<=nj&&ni<n&&nj<m&&!mark[ni][nj]) {
mark[ni][nj] = 1;
if(dfs(ni,nj,L,R))return 1;
mark[ni][nj] = 0;
}
}
return 0;
}
int main() {
ios::sync_with_stdio(0); cin.tie(0);
cin>>n>>m>>k;
for(int t=0;t<n;t++)cin>>A[t];
mark[0][0]=1;
cout<<(dfs(0,0,0,0)?"Yes":"No");
}
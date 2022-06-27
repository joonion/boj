#include <bits/stdc++.h>
using namespace std;
map<char,int>H={{'U',0},{'R',1},{'D',2},{'L',3}};
int a[]={-1,0,1,0},b[]={0,1,0,-1},n,m,k,A[150][150],M[150][150][1501];
struct node{int i,j,l,r;bool operator<(const node &o)const{return r > o.r;}};priority_queue<node> PQ;
bool move(int t,node &u,node &v){int x=A[u.i][u.j];v.l=u.l;v.r=u.r;if(1<=t&&t<=3){x=(x-t+4)%4;v.l+=t;}if(4<=t&&t<=6){x=(x+t-3)%4;v.r+=t-3;}v.i=u.i+a[x];v.j=u.j+b[x];return 0<=v.i&&v.i<n&&0<=v.j&&v.j<m&&v.l<=k&&v.r<=k;}
int bfs(){fill(&M[0][0][0],&M[149][149][1500],1501);PQ.push({0,0,0,0});M[0][0][0]=0;while(!PQ.empty()){node u=PQ.top();PQ.pop();for(int t=0;t<7;t++){node v;if(move(t,u,v)&&M[v.i][v.j][v.l]>v.r){if(v.i==n-1&&v.j==m-1)return 1;PQ.push({v.i,v.j,v.l,v.r});M[v.i][v.j][v.l]=v.r;}}}return 0;}
int main(){ios::sync_with_stdio(0);cin.tie(0);cin>>n>>m>>k;string s;for(int i=0;i<n;i++) {cin>>s;for(int j=0;j<m;j++)A[i][j]=H[s[j]];}cout<<(bfs()?"Yes":"No");}

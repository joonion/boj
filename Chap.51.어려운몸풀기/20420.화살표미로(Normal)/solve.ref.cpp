#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define xx first
#define yy second
#define all(v) (v).begin(), (v).end()

const int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

struct node {
    int x, y, d1, d2;
};

bool operator < (const node &a, const node &b){
    return a.d2 > b.d2;
}

int n, m, k;
int dist[150][150][1501];
char board[150][155];

priority_queue<node> q;

void chk(int x, int y, int d1, int d2){
    if (d1 > k || d2 > k) return;
    if (dist[x][y][d1] > d2) {
        dist[x][y][d1] = d2;
        q.push({x, y, d1, d2});
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> n >> m >> k;

    for (int i = 0; i < n; ++i) 
        cin >> board[i];

    fill(&dist[0][0][0], &dist[150][0][0], 3000);

    dist[0][0][0] = 0;
    q.push({0, 0, 0, 0});

    while(!q.empty()) {
        // auto [x, y, d1, d2] = q.top();
        struct node v = q.top();
        int x, y, d1, d2;
        x = v.x; y = v.y; d1 = v.d1; d2 = v.d2;

        if(x == n - 1 && y == m - 1) {
            cout << "Yes";
            return 0;
        }
        q.pop();

        if(dist[x][y][d1] != d2) 
            continue;
        
        int i;
        if(board[x][y] == 'U') i = 0;
        else if(board[x][y] == 'R') i = 1;
        else if(board[x][y] == 'D') i = 2;
        else i = 3;

        for (int j = 0; j < 4; ++j) {
            int nx = x + dir[i][0], ny = y + dir[i][1];
            ++i; if(i == 4) i = 0;
            if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            chk(nx, ny, d1+j, d2);
            chk(nx, ny, d1, d2+4-j);
        }
    }
    cout << "No";
}

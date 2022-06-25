#include <bits/stdc++.h>
using namespace std;

string DIR = "URDL";
int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

int n, m, k, maze[150][150], dist[150][150][1501];

struct node {
    int i, j, l, r;
};

struct cmp {
    inline bool operator() (const node &a, const node &b) const {
        if (a.i + a.j == b.i + b.j)
            return abs(a.i - a.j) > abs(b.i - b.j);
        else
            return a.i + a.j < b.i + b.j;
    }
};

priority_queue<node, vector<node>, cmp> PQ;

bool move(int t, node &u, node &v) {
    int x = maze[u.i][u.j];
    v.l = u.l; v.r = u.r;
    if (1 <= t && t <= 3) {
        x = (x - t + 4) % 4; v.l += t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4; v.r += t - 3;
    }
    v.i = u.i + di[x]; v.j = u.j + dj[x];
    return 0 <= v.i && v.i < n && 0 <= v.j && v.j < m && v.l <= k && v.r <= k;
}

bool solve() {
    node u = {0, 0, 0, 0};
    PQ.push(u);
    memset(dist, 0x3f3f3f3f, sizeof(dist));
    dist[u.i][u.j][u.l] = u.r;
    while (!PQ.empty()) {
        node u = PQ.top(); PQ.pop();
        // cout << "pop " << u.i << u.j << u.l << u.r << endl;
        if (dist[u.i][u.j][u.l] != u.r)
            continue;
        if (u.i == n - 1 && u.j == m - 1)
            return true;
        for (int t = 0; t < 7; t++) {
            node v;
            if (move(t, u, v) && dist[v.i][v.j][v.l] > v.r) {
                PQ.push(v);
                dist[v.i][v.j][v.l] = v.r;
                // cout << "  push " << v.i << v.j << v.l << v.r << endl;
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        for (int j = 0; j < m; j++)
            maze[i][j] = DIR.find(s[j]);
    }
    cout << (solve() ? "Yes" : "No");
}
#include <bits/stdc++.h>
using namespace std;

string D = "URDL";
int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;

struct edge {
    int v, l, r;
    edge(int V, int L, int R) : v(V), l(L), r(R) {}
    bool operator < (const edge o) { 
        if (l == o.l) return r > o.r; else return l > o.l;
    }
};

vector<vector<edge>> G;
vector<vector<vector<bool>>> mark;

bool move(int t, int v, int &u, int &l, int &r) {
    l = r = 0;
    int i = v / m, j = v % m;
    int x = D.find(A[i][j]);
    if (1 <= t && t <= 3) {
        x = (x >= t) ? (x - t) : (x - t + 4);
        l = t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4;
        r = t - 3;
    }
    int ni = i + di[x], nj = j + dj[x];
    u = ni * m + nj;
    return (0 <= ni && ni < n && 0 <= nj && nj < m && l <= k && r <= k);
}

void build_graph() {
    int V = n * m;
    G.resize(V);
    for (int v = 0; v < V; v++)
        for (int t = 0; t < 7; t++) {
            int u, l, r;
            if (move(t, v, u, l, r))
                G[v].push_back(edge(u, l, r));
        }
}

void print_graph() {
    for (int v = 0; v < G.size(); v++) {
        cout << v << ": ";
        for (int u = 0; u < G[v].size(); u++)
            cout << "(" << G[v][u].v << "," << 
                           G[v][u].l << "," <<
                           G[v][u].r << ") ";
        cout << endl;
    }
}

bool solve() {
    build_graph();
    queue<edge> queue;
    queue.push(edge(0, 0, 0));
    mark.resize(n * m, vector<vector<bool>>(k + 1, vector<bool>(k + 1, false)));
    mark[0][0][0] = true;
    int depth = 0, L = 0, R = 0;
    while (!queue.empty()) {
        edge e = queue.front(); queue.pop();
        if (e.v == n * m - 1) return true;
        for (int t = 0; t < G[e.v].size(); t++) {
            edge u = G[e.v][t];
            if (!mark[u.v][u.l][u.r]) {
                queue.push(edge(u.v, u.l, u.r));
                mark[u.v][u.l][u.r] = true;
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m >> k;
    A.resize(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    cout << (solve() ? "Yes" : "No");
}
#include <bits/stdc++.h>
using namespace std;

#define INF 1501

string D = "URDL";
int imv[] = {-1, 0, 1, 0};
int jmv[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;

typedef struct edge edge_t;
struct edge {
    char d; int v, l, r;
    edge(int V, char D, int L, int R) : v(V), d(D), l(L), r(R) {}
};

vector<vector<edge_t>> graph;

bool move(int t, int i, int j, int &u, char &d, int &L, int &R) {
    L = R = 0;
    int x = D.find(A[i][j]);
    if (1 <= t && t <= 3) {
        x = (x >= t) ? x - t : x - t + 4;
        L = t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4;
        R = t - 3;
    }
    int ni = i + imv[x], nj = j + jmv[x];
    u = ni * m + nj; d = D[x];
    return (0 <= ni && ni < n && 0 <= nj && nj < m);
}

void build_graph() {
    graph.resize(n);
    for (int v = 0; v < n * m; v++) {
        int i = v / m, j = v % m;
        cout << i << j << endl;
        for (int t = 0; t < 7; t++) {
            int u, L, R; char d;
            if (move(t, i, j, u, d, L, R))
                graph[v].push_back(edge(u, d, L, R));
        }
    }
}

void print_graph() {
    for (int v = 0; v < n * m; v++) {
        for (int u = 0; u < graph[v].size(); u++)
            cout << "(" << graph[v][u].v << graph[v][u].d << graph[v][u].l << graph[v][u].r << ") ";
        cout << endl;
    }
}

bool solve() {
    build_graph();
    print_graph();
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
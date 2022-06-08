#include <bits/stdc++.h>
using namespace std;

const string D = "URDL";
const int imv[] = {-1, 0, 1, 0};
const int jmv[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;
vector<vector<bool>> M;

typedef struct edge edge_t;
struct edge {
    int i, j, l, r;
    edge(int I, int J, int L, int R) : i(I), j(J), l(L), r(R) {}
    bool operator < (const edge_t &o) const {
        return (l + r) > (o.l + o.r);
    }
};

priority_queue<edge_t, vector<edge_t>, less<edge_t>> PQ;

bool move(int t, int i, int j, int l, int r, int &ni, int &nj, int &nl, int &nr) {
    nl = l; nr = r;
    int x = D.find(A[i][j]);
    if (1 <= t && t <= 3) {
        x = (x >= t) ? x - t : x - t + 4;
        nl += t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4;
        nr += t - 3;
    }
    ni = i + imv[x]; nj = j + jmv[x];
    return (0 <= ni && ni < n && 0 <= nj && nj < m && !M[ni][nj] && nl <= k && nr <= k);
}

bool bfs() {
    M.resize(n, vector<bool>(m, false));
    PQ.push(edge(0, 0, 0, 0));
    while (!PQ.empty()) {
        edge_t v = PQ.top(); PQ.pop();
        for (int t = 0; t < 7; t++) {
            int ni, nj, nl, nr;
            if (move(t, v.i, v.j, v.l, v.r, ni, nj, nl, nr)) {
                if (ni == n - 1 && nj == n - 1)
                    return true;
                PQ.push(edge(ni, nj, nl, nr));
            }
        } 
        M[v.i][v.j] = true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m >> k;
    A.resize(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    cout << (bfs() ? "Yes" : "No");
}

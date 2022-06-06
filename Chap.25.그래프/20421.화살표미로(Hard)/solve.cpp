#include <bits/stdc++.h>
using namespace std;

string D = "URDL";
int imv[] = {-1, 0, 1, 0};
int jmv[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;
vector<vector<bool>> M;

typedef struct node node_t;
struct node {
    int i, j, l, r;
    node(int I, int J, int L, int R) : i(I), j(J), l(L), r(R) {}
    bool operator < (const node other) const {
        return (l + r) > (other.l + other.r);
    }
};
priority_queue<node, vector<node>> PQ;

bool move(int t, int i, int j, int L, int R, 
          int &ni, int &nj, int &nL, int &nR)
{
    int x = D.find(A[i][j]); nL = L; nR = R;
    if (1 <= t && t <= 3) {
        x = (x - t) % 4; nL = L + t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4; nR = R + t - 3;
    }
    ni = i + imv[x]; nj = j + jmv[x];
    return (0 <= ni && ni < n && 0 <= nj && nj < m &&
            !M[ni][nj] && nL <= k && nR <= k);
}

bool solve() {
    PQ.push(node(0, 0, 0, 0));
    while (!PQ.empty()) {
        node_t v = PQ.top(); PQ.pop();
        M[v.i][v.j] = true; // visited
        for (int t = 0; t < 7; t++) {
            int ni, nj, nL, nR;
            if (move(t, v.i, v.j, v.l, v.r, ni, nj, nL, nR)) {
                if (ni == n - 1 && nj == m - 1)
                    return true;
                PQ.push(node(ni, nj, nL, nR));
                cout << ni << "," << nj << "," << nL << "," << nR << endl;
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
    M.resize(n, vector<bool>(m, false));
    cout << (solve() ? "Yes" : "No");
}
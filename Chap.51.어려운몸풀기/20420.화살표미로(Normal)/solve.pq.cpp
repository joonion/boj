#include <bits/stdc++.h>
using namespace std;

string D = "URDL";
int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;

struct node {
    int id, L, R; bitset<2500> path;
    node(int ID, int l, int r) : id(ID), L(l), R(r) {}
    bool operator < (const node &other) const {
        if (R == other.R) return L > other.L; else return R > other.R;
    }
};

priority_queue<node> PQ;

bool promising(int t, int v, int &u, int &l, int &r) {
    l = r = 0;
    int i = v / m, j = v % m;
    int x = D.find(A[i][j]);
    if (1 <= t && t <= 3) {
        l = t; 
        x = (x >= t) ? x - t : 4 + x - t;
    }
    if (4 <= t && t <= 6) {
        r = t - 3; 
        x = (x + t - 3) % 4;
    }
    int ni = i + di[x], nj = j + dj[x];
    u = ni * m + nj;
    return (0 <= ni && ni < n && 0 <= nj && nj < m);
}

bool solve() {
    node root(0, 0, 0);
    root.path.set(0);
    PQ.push(root);
    while (!PQ.empty()) {
        node v = PQ.top(); PQ.pop();
        // cout << v.id << " " << v.L << " " << v.R << endl;
        for (int t = 0; t < 7; t++) {
            int u, l, r;
            if (promising(t, v.id, u, l, r)) {
                if (v.L + l <= k && v.R + r <= k) {
                    if (u == n * m - 1) return true;
                    if (!v.path.test(u)) {
                        node newnode(u, v.L + l, v.R + r);
                        newnode.path |= v.path;
                        newnode.path.set(u);
                        PQ.push(newnode);
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    cin >> n >> m >> k;
    A.resize(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    cout << (solve() ? "Yes" : "No");
}
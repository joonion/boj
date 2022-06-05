#include <bits/stdc++.h>
using namespace std;

typedef struct node node_t;
struct node {
    int i; int j; int L; int R;
    node(int a, int b, int c, int d) {i = a; j = b; L = c; R = d;}
    bool operator < (const node_t other) const {
        return (L + R) > (other.L + other.R);
    }
};

int n, m, k;
vector<string> A;
priority_queue<node_t, vector<node_t>> PQ;

bool bfs() {
    node_t s(0, 0, k, k);
    PQ.push(s);
    while (!PQ.empty()) {
        node_t v = PQ.top(); PQ.pop();
        cout << v.i << v.j << v.L << v.R << endl;
        for (int t = 0; t < 7; t++) {
            int i, j, L, R;
            move(t, v, i, j, L, R);
            if (i == n - 1 && j == m - 1)
                return true;
            if (promising(i, j, L, R)) {
                PQ.push(u);
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
    cout << ((bfs()) ? "Yes" : "No");
}
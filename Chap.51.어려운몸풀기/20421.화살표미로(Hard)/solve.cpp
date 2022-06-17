#include <bits/stdc++.h>
using namespace std;

map<char, int> H = {{'U', 0}, {'R', 1}, {'D', 2}, {'L', 3}};

int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

int n, m, k;
int A[150][150];
vector<pair<int, int>> card;

struct node {
    int i, j, l, r;
    bool operator < (const node &o) const {
        if (i + j == o.i + o.j)
            return abs(i - j) > abs(o.i - o.j);
        return i + j < o.i + o.j;
    }
};
priority_queue<node> PQ;

int cnt = 0;

bool move(int t, node &u, node &v) {
    int x = A[u.i][u.j]; v.l = u.l; v.r = u.r;
    if (1 <= t && t <= 3) {
        x = (x - t + 4) % 4; v.l += t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4; v.r += t - 3;
    }
    v.i = u.i + di[x]; v.j = u.j + dj[x];
    return 0 <= v.i && v.i < n && 0 <= v.j && v.j < m && v.l <= k && v.r <= k;
}

bool search() {
    card.resize(n * m, make_pair(1501, 1501));
    PQ.push({0, 0, 0, 0});
    card[0] = make_pair(0, 0);
    while (!PQ.empty()) {
        node u = PQ.top(); PQ.pop();
        cout << "pop " << u.i << u.j << u.l << u.r << endl;
        for (int t = 0; t < 7; t++) {
            node v;
            if (move(t, u, v)) {
                if (v.i == n - 1 && v.j == m - 1)
                    return true;
                pair<int, int> &cur = card[v.i * m + v.j];
                cout << "    cur " << cur.first << cur.second << endl;
                if (v.l < cur.first || v.r < cur.second) {
                    cout << "  push " << v.i << v.j << v.l << v.r << endl;
                    PQ.push(v);
                    cur.first = v.l; cur.second = v.r;
                    cnt++;
                }
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m >> k;
    string s;
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < m; j++)
            A[i][j] = H[s[j]];
    }
    cout << (search() ? "Yes" : "No") << endl;
    cout << cnt << endl;
}
#include <bits/stdc++.h>
using namespace std;

map<char, int> H = {{'U', 0}, {'R', 1}, {'D', 2}, {'L', 3}};

int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

int n, m, k;
int A[50][50];
bool mark[2500];

bool move(int t, int u, int l, int r, int &v, int &L, int &R) {
    int i = u / m, j = u % m;
    int x = A[i][j]; L = l; R = r;
    if (t == 1) {
        x = (x + 3) % 4; L++;
    }
    if (t == 2) {
        x = (x + 1) % 4; R++;
    }
    int ni = i + di[x], nj = j + dj[x];
    v = ni * m + nj;
    return 0 <= ni && ni < n && 0 <= nj && nj < m && L <= k && R <= k;
}

bool dfs(int u, int l, int r) {
    if (u == n * m - 1)
        return true;
    for (int t = 0; t < 3; t++) {
        int v, L, R;
        if (move(t, u, l, r, v, L, R) && !mark[v]) {
            mark[v] = true;
            if (dfs(v, L, R))
                return true;
            mark[v] = false;
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
    fill(&mark[0], &mark[2500], false);
    mark[0] = true;
    cout << (dfs(0, 0, 0) ? "Yes" : "No");
}
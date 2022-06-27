#include <bits/stdc++.h>
using namespace std;

map<char, int> H = {{'U', 0}, {'R', 1}, {'D', 2}, {'L', 3}};

int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

int n, m, k;
string A[50];
bool mark[50][50];

bool dfs(int i, int j, int l, int r) {
    if (i == n - 1 && j == m - 1)
        return true;
    for (int t = 0; t < 3; t++) {
        int L = l, R = r, x = H[A[i][j]];
        if (t == 1) {
            x = (x + 3) % 4; L++;
        } else if (t == 2) {
            x = (x + 1) % 4; R++;
        }
        int ni = i + di[x], nj = j + dj[x];
        if (L <= k && R <= k && 0 <= ni && 0 <= nj && ni < n && nj < m && !mark[ni][nj]) {
            mark[ni][nj] = true;
            if (dfs(ni, nj, L, R))
                return true;
            mark[ni][nj] = false;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++)
        cin >> A[i];
    mark[0][0] = true;
    cout << (dfs(0, 0, 0, 0) ? "Yes" : "No");
}
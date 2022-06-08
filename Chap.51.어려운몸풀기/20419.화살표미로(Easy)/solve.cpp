#include <bits/stdc++.h>
using namespace std;

const string DIR = "URDL";
const int imov[] = {-1, 0, 1, 0};
const int jmov[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;
vector<vector<bool>> M;

bool promising(int t, int i, int j, int L, int R, 
               int &ni, int &nj, int &nL, int &nR)
{
    int x = DIR.find(A[i][j]); nL = L; nR = R;
    if (1 <= t && t <= 3) { // rotate left
        x = (x - t) % 4; nL = L - t;
    }
    if (4 <= t && t <= 6) { // rotate right
        x = (x + t - 3) % 4; nR = R - t + 3;
    }
    ni = i + imov[x]; nj = j + jmov[x];
    return (0 <= ni && ni < n && 0 <= nj && nj < m && 
            !M[ni][nj] && nL >= 0 && nR >= 0);
}

bool dfs(int i, int j, int L, int R) {
    if (i == n - 1 && j == m - 1)
        return true;
    else {
        int ni, nj, nL, nR;
        for (int t = 0; t < 7; t++) {
            if (promising(t, i, j, L, R, ni, nj, nL, nR)) {
                M[ni][nj] = true;
                if (dfs(ni, nj, nL, nR))
                    return true;
                M[ni][nj] = false;
            }
        }
        return false;
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m >> k;
    A.resize(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    M.resize(n, vector<bool>(m, false));
    M[0][0] = true;
    cout << (dfs(0, 0, k, k) ? "Yes" : "No");
}
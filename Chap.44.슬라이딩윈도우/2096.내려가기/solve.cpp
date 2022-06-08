#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> A;

int minimum() {
    if (n == 1)
        return min(A[0][0], min(A[0][1], A[0][2]));
    else {
        vector<vector<int>> D(2, vector<int>(3, 0));
        int cur, nxt;
        for (int i = n - 1; i >= 0; i--) {
            cur = i % 2; nxt = abs((i - 1) % 2);
            D[nxt][0] = A[i][0] + min(D[cur][0], D[cur][1]);
            D[nxt][1] = A[i][1] + min(D[cur][0], min(D[cur][1], D[cur][2]));
            D[nxt][2] = A[i][2] + min(D[cur][1], D[cur][2]);
        }
        return min(D[1][0], min(D[1][1], D[1][2]));
    }
}

int maximum() {
    if (n == 1)
        return max(A[0][0], max(A[0][1], A[0][2]));
    else {
        vector<vector<int>> D(2, vector<int>(3, 0));
        int cur, nxt;
        for (int i = n - 1; i >= 0; i--) {
            cur = i % 2; nxt = abs((i - 1) % 2);
            D[nxt][0] = A[i][0] + max(D[cur][0], D[cur][1]);
            D[nxt][1] = A[i][1] + max(D[cur][0], max(D[cur][1], D[cur][2]));
            D[nxt][2] = A[i][2] + max(D[cur][1], D[cur][2]);
        }
        return max(D[1][0], max(D[1][1], D[1][2]));
    }
}

int main() {
    cin >> n;
    A.resize(n, vector<int>(3));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < 3; j++)
            cin >> A[i][j];
    cout << maximum() << " " << minimum() << endl;
}
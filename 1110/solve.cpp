#include <iostream>
using namespace std;

int solve(int n) {
    int m = n;
    int cnt = 1;
    while (true) {
        int s = 0, t = m;
        while (t != 0) {
            s += t % 10;
            t /= 10;
        }
        m = (m % 10) * 10 + (s % 10);
        if (m == n)
            break;
        cnt++;
    }
    return cnt;
}

int main() {
    int N; cin >> N;
    int answer = solve(N);
    cout << answer << endl;
}
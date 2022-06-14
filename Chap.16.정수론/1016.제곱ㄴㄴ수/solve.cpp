#include <bits/stdc++.h>
using namespace std;
typedef long long long_t;
int main() {
    long_t n, m; cin >> n >> m;
    vector<bool> sieve(m - n + 1, true);
    for (long_t k = 2; k * k <= m; k++) {
        long_t s = k * k;
        long_t i = (n % s) ? (s - (n % s)) : 0;
        for (long_t j = i; j < sieve.size(); j += s)
            sieve[j] = false;
    }
    int cnt = 0;
    for (int i = 0; i < sieve.size(); i++)
        if (sieve[i]) cnt++;
    cout << cnt;
}
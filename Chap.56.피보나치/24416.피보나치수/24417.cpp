#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull_t;
int cnt1, cnt2;

int fib1(int n) {
    if (n == 1 || n == 2) {
        cnt1++; return 1;
    } else {
        return fib1(n-1) + fib1(n-2);
    }
}

int fib2(int n) {
    int a = 1, b = 1;
    for (int i = 3; i <= n; i++) {
        int t = (a + b) % 1000000007;
        a = b; b = t; cnt2++;
    }
    return b;
}

int main() {
    int n; cin >> n;
    int f = fib2(n);
    cout << f << " " << n - 2 << endl;
}
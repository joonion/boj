#include <bits/stdc++.h>
using namespace std;

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
        int t = a + b;
        a = b; b = t; cnt2++;
    }
    return b;
}

int main() {
    int n; cin >> n;
    fib1(n); fib2(n);
    cout << cnt1 << " " << cnt2 << endl;
}
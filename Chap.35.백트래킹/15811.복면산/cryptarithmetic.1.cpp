#include <bits/stdc++.h>
using namespace std;

string a, b, c, d;
vector<int> v = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

bool solve() {
    int n = d.size();
    do {
        for (int i = 0; i < n; i++)
            cout << v[i] << " ";
        cout << endl;
        
        reverse(v.begin() + n, v.end());
    } while (next_permutation(v.begin(), v.end()));
}

int main() {
    cin >> a >> b >> c;
    for (char c: a) 
        if (find(d.begin(), d.end(), c) == d.end())
            d += c;
    for (char c: b) 
        if (find(d.begin(), d.end(), c) == d.end())
            d += c;
    for (char c: c) 
        if (find(d.begin(), d.end(), c) == d.end())
            d += c;
    cout << d << endl;
    solve();
}
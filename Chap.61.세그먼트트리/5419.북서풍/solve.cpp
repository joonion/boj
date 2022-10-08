#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> coord;

int compress(vector<coord> &p) {
    set<int> q; map<int,int> m;
    for (int i = 0; i < p.size(); i++)
        q.insert(p[i].second);
    auto it = q.begin();
    for (int i = 0; i < q.size(); i++, it++)
        m[*it] = i + 1;
    for (int i = 0; i < p.size(); i++)
        p[i].second = m[p[i].second];
    return q.size();
}

bool compare(coord a, coord b) {
    if (a.first == b.first)
        return a.second > b.second;
    return a.first < b.first;
}

void update(int v, int l, int r, int pos, vector<int> &T) {
    if (l == r)
        T[v] += 1;
    else {
        int m = (l + r) / 2;
        if (pos <= m)
            update(2*v, l, m, pos, T);
        else
            update(2*v+1, m+1, r, pos, T);
        T[v] = T[2*v] + T[2*v+1];
    }
}

int query(int v, int l, int r, int L, int R, vector<int> &T) {
    if (r < L || R < l)
        return 0;
    else if (L <= l && r <= R)
        return T[v];
    else {
        int m = (l + r) / 2;
        return query(2*v, l, m, L, R, T) +
               query(2*v+1, m+1, r, L, R, T);
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    while (T--) {
        int n; cin >> n;
        vector<coord> p(n);
        for (int i = 0; i < n; i++)
            cin >> p[i].first >> p[i].second;
        int size = compress(p);
        sort(p.begin(), p.end(), compare);
        vector<int> T(4*n+1, 0);
        int s = 0;
        for (int i = 0; i < n; i++) {
            s += query(1, 1, n, p[i].second, n, T);
            update(1, 1, n, p[i].second, T);
        }
        cout << s << endl;
    }
}
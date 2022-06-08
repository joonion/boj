#include <bits/stdc++.h>
using namespace std;

#define INF 1501

string D = "URDL";
int imv[] = {-1, 0, 1, 0};
int jmv[] = {0, 1, 0, -1};

int n, m, k;
vector<string> A;

typedef pair<int, int> pair_t;

typedef struct edge edge_t;
struct edge {
    int i, j, l, r; bool mark;
    edge(int I, int J, int L, int R) : i(I), j(J), l(L), r(R) {mark = false;}
};

vector<vector<vector<edge_t>>> graph;

vector<vector<pair_t>> pathlength;

bool move(int t, int i, int j, int &ni, int &nj, int &nl, int &nr) {
    nl = nr = 0;
    int x = D.find(A[i][j]);
    if (1 <= t && t <= 3) {
        x = (x >= t) ? x - t : x - t + 4;
        nl = t;
    }
    if (4 <= t && t <= 6) {
        x = (x + t - 3) % 4;
        nr = t - 3;
    }
    ni = i + imv[x]; nj = j + jmv[x];
    return (0 <= ni && ni < n && 0 <= nj && nj < m);
}

void print_graph(vector<vector<vector<edge_t>>> graph) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            cout << i << "," << j << ":";
            for (int t = 0; t < graph[i][j].size(); t++) {
                cout << "(" <<
                    graph[i][j][t].i << "," <<
                    graph[i][j][t].j << "," <<
                    graph[i][j][t].l << "," <<
                    graph[i][j][t].r << ") ";
            }
            cout << endl;
        }
}

pair_t minlength(int si, int sj, int di, int dj) {
    if (si == di && sj == dj)
        return make_pair(0, 0);
    int ai = abs(si - di), aj = abs(sj - dj);
    if (ai > 1 || aj > 1 || ai + aj == 2)
        return make_pair(INF, INF);
    pair_t mlength = make_pair(INF, INF);
    for (int i = 0; i < graph[si][sj].size(); i++) {
        edge_t edge = graph[si][sj][i];
        if (edge.i == di && edge.j == dj && mlength.first + mlength.second > edge.l + edge.r)
            mlength = make_pair(edge.l, edge.r);
    }
    return mlength;
}

void print_length(vector<vector<pair_t>> length) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cout << "(" << length[i][j].first << "," << length[i][j].second << ") ";
    cout << endl;
}

pair_t bypasslength(int vneari, int vnearj, int i, int j) {
    pair_t temp = minlength(vneari, vnearj, i, j);
    temp.first += pathlength[vneari][vnearj].first;
    temp.second += pathlength[vneari][vnearj].second;
    temp.first = (temp.first >= INF) ? INF : temp.first;    
    temp.second = (temp.second >= INF) ? INF : temp.second;    
    return temp;
}

bool solve() {

    // make a graph with multiple edges
    graph.resize(n, vector<vector<edge_t>>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            for (int t = 0; t < 7; t++) {
                int ni, nj, nl, nr;
                if (move(t, i, j, ni, nj, nl, nr))
                    graph[i][j].push_back(edge(ni, nj, nl, nr));
            }
    // print_graph(graph);

    // search a path from the source to the destination
    pathlength.resize(n, vector<pair_t>(m, make_pair(INF, INF)));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            pathlength[i][j] = minlength(0, 0, i, j);
    print_length(pathlength);

    vector<vector<bool>> mark(n, vector<bool>(m, false));
    mark[0][0] = true;

    for (int t = 0; t < n * m - 1; t++) {
        pair_t minlen = make_pair(INF, INF);
        int vneari, vnearj;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (mark[i][j]) continue;
                if (pathlength[i][j].first + pathlength[i][j].second < minlen.first + minlen.second) {
                    minlen = pathlength[i][j];
                    vneari = i; vnearj = j;
                }
            }
        cout << vneari << "," << vnearj << endl;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                pair_t bypasslen = bypasslength(vneari, vnearj, i, j);
                if (pathlength[i][j].first + pathlength[i][j].second > bypasslen.first + bypasslen.second)
                    pathlength[i][j] = bypasslen;
            }
        mark[vneari][vnearj] = true;
        print_length(pathlength);
    }


    return false;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m >> k;
    A.resize(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    cout << (solve() ? "Yes" : "No");
}
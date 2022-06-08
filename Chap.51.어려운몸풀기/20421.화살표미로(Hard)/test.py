#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

const int INF = 0x3f3f3f3f;
int n, m, k;
int board[150][150];

enum { R, U, L, D };
int conv(char c) {
	switch (c) {
	case 'R': return R;
	case 'U': return U;
	case 'L': return L;
	case 'D': return D;
	}
}

struct Edge {
	int x, y, cost_r, cost_l; //destination, cost
};
vector<Edge> adj[150][150];

struct Info {
	int r, l, x, y; //cost_r, cur
	bool operator < (const Info& I) const {
		return r < I.r;
	}
	bool operator > (const Info& I) const {
		return I < *this;
	}
};
int dist[1501][150][150]; //cost_l, x, y

bool OOB(int x, int y) { return x < 0 || x >= n || y < 0 || y >= m; }

int main() {
	fastio;
	//input
	memset(dist, 0x3f, sizeof(dist));
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		string s; cin >> s;
		for (int j = 0; j < m; j++) {
			board[i][j] = conv(s[j]);
		}
	}

	//graph construction
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
		int d = board[i][j];
		for (int k = 0; k < 4; k++) { //cw
			int nx = i + "1012"[(d - k + 4) % 4] - '1';
			int ny = j + "2101"[(d - k + 4) % 4] - '1';
			if (OOB(nx, ny)) continue;
			adj[i][j].push_back({ nx, ny, k, 0 });
		}
		for (int k = 0; k < 4; k++) { //ccw
			int nx = i + "1012"[(d + k) % 4] - '1';
			int ny = j + "2101"[(d + k) % 4] - '1';
			if (OOB(nx, ny)) continue;
			adj[i][j].push_back({ nx, ny, 0, k });
		}
	}

	//dijkstra
	priority_queue<Info, vector<Info>, greater<Info>> PQ;
	dist[0][0][0] = 0;
	PQ.push({ 0, 0, 0, 0 });
	while (!PQ.empty()) {
		auto [r, l, x, y] = PQ.top(); PQ.pop();
		if (dist[l][x][y] != r) continue;
		if (x == n - 1 && y == m - 1) {
			cout << "Yes" << '\n';
			return 0;
		}
		for (auto [nx, ny, cost_r, cost_l] : adj[x][y]) {
			if (r + cost_r > k || l + cost_l > k) continue;
			if (dist[l + cost_l][nx][ny] > r + cost_r) {
				dist[l + cost_l][nx][ny] = r + cost_r;
				PQ.push({ r + cost_r, l + cost_l, nx, ny });
			}
		}
	}
	cout << "No" << '\n';
}
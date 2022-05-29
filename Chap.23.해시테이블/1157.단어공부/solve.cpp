#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

char solve(string word) {
    vector<int> freq(26, 0);
    for (char ch: word)
        freq[toupper(ch) - 'A']++;

    int best = *max_element(freq.begin(), freq.end());
    int answer = -1;
    for (int i = 0; i < 26; i++)
        if (freq[i] == best)
            if (answer != -1)
                return '?';
            else
                answer = i;
    return 'A' + answer;
}

int main() {
    string s; cin >> s;
    char answer = solve(s);
    cout << answer << endl;
}